"""Conservative, byte-preserving local Markdown section-body replacement."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import tempfile


class UpdateError(ValueError):
    pass


HEADING = re.compile(rb"^ {0,3}(#{1,6})(?:[ \t]+(.*)|[ \t]*)$")
FENCE = re.compile(rb"^ {0,3}(`{3,}|~{3,})(.*)$")
SETEXT = re.compile(rb"^ {0,3}(?:=+|-+)[ \t]*$")


def sections(data):
    try:
        data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise UpdateError("Draft must be UTF-8; no write performed.") from exc
    headings = []
    offset = 0
    fence = None
    for line in data.splitlines(keepends=True):
        raw = line.rstrip(b"\r\n")
        fm = FENCE.match(raw)
        if fence:
            char, length = fence
            if re.fullmatch(rb" {0,3}" + re.escape(char) + rb"{" + str(length).encode() + rb",}[ \t]*", raw):
                fence = None
        elif fm:
            marks, tail = fm.groups()
            if marks.startswith(b"`") and b"`" in tail:
                raise UpdateError("Ambiguous backtick fence; no write performed.")
            fence = (marks[:1], len(marks))
        elif SETEXT.match(raw):
            raise UpdateError("Setext/thematic-rule candidate unsupported; no write performed.")
        else:
            hm = HEADING.match(raw)
            if hm:
                title = hm.group(2) or b""
                title = re.sub(rb"[ \t]+#+[ \t]*$", b"", title).strip(b" \t")
                headings.append({"title": title.decode("utf-8"), "level": len(hm.group(1)),
                                 "start": offset, "body": offset + len(line), "heading": line})
        offset += len(line)
    if fence:
        raise UpdateError("Unclosed fence; no write performed.")
    if not headings or headings[0]["level"] != 1 or sum(h["level"] == 1 for h in headings) != 1:
        raise UpdateError("Expected exactly one H1 document title first; no write performed.")
    names = [h["title"] for h in headings]
    if len(set(names)) != len(names):
        raise UpdateError("Duplicate heading titles are ambiguous; no write performed.")
    for index, heading in enumerate(headings):
        heading["end"] = headings[index + 1]["start"] if index + 1 < len(headings) else len(data)
    return headings


def plan_update(original, updates, allowed, replace_existing, expected_sha256):
    if not replace_existing:
        raise UpdateError("Existing-file replacement permission is missing; ask before writing.")
    if hashlib.sha256(original).hexdigest() != expected_sha256:
        raise UpdateError("Draft digest differs from the reviewed snapshot; reread before writing.")
    if not isinstance(updates, dict) or not updates or not all(isinstance(k, str) and isinstance(v, str) for k, v in updates.items()):
        raise UpdateError("Updates must be a nonempty JSON object of title-to-body strings.")
    if set(updates) - set(allowed):
        raise UpdateError("A requested section is unauthorized; ask for permission. No changes made.")
    old = sections(original)
    lookup = {h["title"]: h for h in old}
    if set(updates) - set(lookup):
        raise UpdateError("A requested section is absent; no sections may be added.")
    if old[0]["title"] in updates:
        raise UpdateError("The document title and its body are protected.")
    parts = []
    cursor = 0
    for heading in old:
        title = heading["title"]
        if title not in updates:
            continue
        body = updates[title].encode("utf-8")
        if heading["end"] < len(original) and body and not body.endswith(b"\n"):
            raise UpdateError("Replacement before another heading must end in a newline.")
        parts.extend((original[cursor:heading["body"]], body))
        cursor = heading["end"]
    parts.append(original[cursor:])
    result = b"".join(parts)
    new = sections(result)
    if [(h["title"], h["level"], h["heading"]) for h in new] != [(h["title"], h["level"], h["heading"]) for h in old]:
        raise UpdateError("Replacement would change or add headings; no write performed.")
    if original[:old[0]["start"]] != result[:new[0]["start"]]:
        raise UpdateError("Protected preamble changed; no write performed.")
    for before, after in zip(old, new):
        if before["title"] not in updates and original[before["body"]:before["end"]] != result[after["body"]:after["end"]]:
            raise UpdateError("Protected body changed; no write performed.")
    return result


def apply_update(path, updates, allowed, replace_existing, expected_sha256):
    path = Path(path)
    if path.is_symlink():
        raise UpdateError("Symlink drafts are unsupported; no write performed.")
    original = path.read_bytes()
    result = plan_update(original, updates, allowed, replace_existing, expected_sha256)
    if result == original:
        return {"changed": False, "sections": [], "sha256": expected_sha256}
    mode = stat.S_IMODE(path.stat().st_mode)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".brief-update-", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(result)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary, mode)
        if path.is_symlink() or path.read_bytes() != original:
            raise UpdateError("Draft changed before commit; no write performed.")
        os.replace(temporary, path)
        temporary = None
    finally:
        if temporary is not None:
            temporary.unlink()
    if path.read_bytes() != result:
        raise UpdateError("Post-write verification failed; inspect the current file before retrying.")
    return {"changed": True, "sections": list(updates), "sha256": hashlib.sha256(result).hexdigest()}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise UpdateError("Duplicate update keys are not allowed.")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft")
    parser.add_argument("--updates", required=True)
    parser.add_argument("--allow-section", action="append", default=[])
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--replace-existing", action="store_true")
    args = parser.parse_args()
    try:
        updates = json.loads(Path(args.updates).read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        report = apply_update(args.draft, updates, args.allow_section, args.replace_existing, args.expected_sha256)
        print(json.dumps(report))
    except (OSError, ValueError, UnicodeError) as exc:
        parser.exit(2, "Update stopped: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
