#!/usr/bin/env python3
"""Mechanical, permission-explicit editor for direct bodies under ATX headings.

Usage: python3 update_sections.py DRAFT PLAN --allow SECTION [--allow SECTION]
       Add --apply --replace-existing only with explicit replacement authority.
PLAN is a JSON object {"Heading text": "complete body, including blank lines\n"}.
Dry-run is default. Error exits 2 without writing the draft before commit.
Uses Python 3 standard library. Does not assess factual support or citations.
"""
import argparse
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile


def safe_path(value):
    path = Path(value).absolute()
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError("Symlinked paths are unsupported: " + str(part))
    if not path.is_file():
        raise ValueError("Expected an existing regular file: " + str(path))
    return path


def headings(data):
    data.decode("utf-8")
    if data.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is unsupported; preserve the draft and clarify")
    lines = data.splitlines(keepends=True)
    if lines and lines[0].rstrip(b"\r\n") in (b"---", b"+++"):
        raise ValueError("Front matter is unsupported")
    out = []
    offset = 0
    fence = None
    for line in lines:
        body = line.rstrip(b"\r\n")
        marker = re.match(rb"^ {0,3}(`{3,}|~{3,})(.*)$", body)
        if fence:
            if marker and marker[1][:1] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            offset += len(line)
            continue
        if marker:
            fence = (marker[1][:1], len(marker[1]))
            offset += len(line)
            continue
        if re.match(rb"^ {0,3}(?:=+|-+)[ \t]*$", body):
            raise ValueError("Setext headings or ambiguous divider syntax are unsupported")
        match = re.match(rb"^ {0,3}(#{1,6})(?:[ \t]+|$)(.*)$", body)
        if match:
            title = re.sub(rb"[ \t]+#+[ \t]*$", b"", match[2]).strip().decode("utf-8")
            out.append((title, len(match[1]), offset, offset + len(line)))
        offset += len(line)
    if fence:
        raise ValueError("Unclosed fenced code block")
    return out


def newline_style(data):
    if b"\r" in data.replace(b"\r\n", b""):
        raise ValueError("Unsupported bare CR newline")
    if b"\r\n" in data and b"\n" in data.replace(b"\r\n", b""):
        raise ValueError("Mixed newline conventions are unsupported")
    return b"\r\n" if b"\r\n" in data else b"\n"


def make_update(original, replacements, allowed):
    if not isinstance(replacements, dict) or not replacements:
        raise ValueError("Plan must be a nonempty JSON object")
    if not all(isinstance(k, str) and isinstance(v, str) for k, v in replacements.items()):
        raise ValueError("Plan keys and bodies must be strings")
    denied = set(replacements) - set(allowed)
    if denied:
        raise ValueError("Requested section lacks authority: " + ", ".join(sorted(denied)))
    eol = newline_style(original)
    before = headings(original)
    spans = []
    for name, body in replacements.items():
        matches = [(i, h) for i, h in enumerate(before) if h[0] == name]
        if len(matches) != 1:
            raise ValueError("Section missing or ambiguous: " + name)
        i, heading = matches[0]
        if heading[1] == 1 or i == 0:
            raise ValueError("Document title/introduction cannot be replaced")
        if b"\n" not in original[heading[2]:heading[3]]:
            raise ValueError("Target heading has no line terminator")
        if "\r" in body:
            raise ValueError("Plan bodies must use LF, not CR")
        replacement = body.encode("utf-8").replace(b"\n", eol)
        if headings(replacement):
            raise ValueError("Replacement body contains a heading")
        end = before[i + 1][2] if i + 1 < len(before) else len(original)
        if replacement and end < len(original) and not replacement.endswith(eol):
            raise ValueError("Body must end with a newline before the next heading")
        spans.append((heading[3], end, replacement))
    spans.sort()
    chunks = []
    cursor = 0
    for start, end, replacement in spans:
        chunks.extend((original[cursor:start], replacement))
        cursor = end
    chunks.append(original[cursor:])
    updated = b"".join(chunks)
    after = headings(updated)
    if [(h[0], h[1]) for h in before] != [(h[0], h[1]) for h in after]:
        raise ValueError("Heading structure changed")
    # Verify a byte mask: replace each authorized body with the same sentinel.
    def protected(data, hs):
        result = []
        cursor = 0
        for i, h in enumerate(hs):
            if h[0] in replacements:
                end = hs[i + 1][2] if i + 1 < len(hs) else len(data)
                result.extend((data[cursor:h[3]], b"\x00AUTHORIZED-BODY\x00"))
                cursor = end
        result.append(data[cursor:])
        return b"".join(result)
    if protected(original, before) != protected(updated, after):
        raise ValueError("Protected bytes changed")
    return updated


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate plan key: " + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft")
    parser.add_argument("plan")
    parser.add_argument("--allow", action="append", default=[])
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--replace-existing", action="store_true")
    args = parser.parse_args()
    try:
        if args.apply and not args.replace_existing:
            raise ValueError("Existing-file replacement authority is missing")
        path = safe_path(args.draft)
        plan_path = safe_path(args.plan)
        original = path.read_bytes()
        plan = json.loads(plan_path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        updated = make_update(original, plan, args.allow)
        digest = hashlib.sha256(original).hexdigest()
        if not args.apply:
            sys.stdout.writelines(difflib.unified_diff(original.decode().splitlines(True), updated.decode().splitlines(True), fromfile=str(path), tofile=str(path) + " (proposed)"))
            print("DRY RUN: draft unchanged; original SHA256=" + digest)
            return 0
        if safe_path(args.draft) != path or path.read_bytes() != original:
            raise ValueError("Draft changed during preparation; inspect before retrying")
        if updated == original:
            print("NO CHANGE: authorized bodies already match")
            return 0
        # An interrupted write can leave this temporary artifact; inspect before retrying.
        with tempfile.NamedTemporaryFile(prefix=".release-brief-update-", suffix=".tmp", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(updated)
            stream.flush()
            os.fsync(stream.fileno())
        if path.read_bytes() != original or path.is_symlink():
            raise ValueError("Draft changed before commit; draft not replaced; temporary file retained: " + str(temporary))
        os.replace(temporary, path)
        if path.read_bytes() != updated:
            raise ValueError("Post-write verification failed; inspect actual draft before retrying")
        print("UPDATED: " + str(path) + "; sections=" + ", ".join(plan) + "; protected bytes verified; original SHA256=" + digest)
        return 0
    except (ValueError, OSError, UnicodeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
