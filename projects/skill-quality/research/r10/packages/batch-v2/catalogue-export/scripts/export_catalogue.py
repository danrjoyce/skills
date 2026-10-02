#!/usr/bin/env python3
"""Strict, preflighted local catalogue export. Python standard library only."""
import argparse
import json
import os
import re
import stat
import sys

ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z", re.ASCII)
LINE_BREAKS = frozenset("\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029")


class Invalid(ValueError):
    pass


def single_line(value):
    return isinstance(value, str) and not any(c in LINE_BREAKS for c in value)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise Invalid("Duplicate JSON key: " + repr(key))
        result[key] = value
    return result


def bad_constant(value):
    raise Invalid("Nonstandard JSON constant: " + value)


def render(input_path):
    with open(input_path, "r", encoding="utf-8") as source:
        data = json.load(source, object_pairs_hook=unique_object,
                         parse_constant=bad_constant)
    if not isinstance(data, list):
        raise Invalid("Input must be a JSON array")
    records, seen = [], set()
    for number, item in enumerate(data, 1):
        if not isinstance(item, dict) or set(item) != {"id", "title", "tags"}:
            raise Invalid(f"Record {number}: expected exactly id, title, tags")
        ident, title, tags = item["id"], item["title"], item["tags"]
        if not isinstance(ident, str) or ID.fullmatch(ident) is None:
            raise Invalid(f"Record {number}: invalid id")
        if ident in seen:
            raise Invalid(f"Record {number}: duplicate id {ident!r}")
        seen.add(ident)
        if not single_line(title) or not title:
            raise Invalid(f"Record {number}: title must be a nonempty single line")
        if not isinstance(tags, list) or not all(single_line(tag) for tag in tags):
            raise Invalid(f"Record {number}: tags must be an array of single-line strings")
        normalized = sorted({tag.strip().lower() for tag in tags} - {""})
        records.append({"id": ident, "title": title, "tags": normalized,
                        "file": ident + ".md"})
    records.sort(key=lambda item: item["id"])
    outputs = []
    for record in records:
        tags_text = ", ".join(record["tags"]) or "(none)"
        body = f"# {record['title']}\n\nTags: {tags_text}\n"
        outputs.append((record["file"], body.encode("utf-8")))
    index = (json.dumps(records, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    outputs.append(("index.json", index))
    return outputs


def open_destination(path):
    if (not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY")
            or any(fn not in os.supports_dir_fd for fn in (os.open, os.stat, os.unlink))):
        raise Invalid("Host lacks required POSIX no-follow directory operations")
    if ".." in path.split(os.sep):
        raise Invalid("Destination must not contain '..'; provide a direct authorized path")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    absolute = os.path.abspath(path)
    fd = os.open(os.sep, flags)
    try:
        for component in absolute.split(os.sep):
            if not component:
                continue
            next_fd = os.open(component, flags, dir_fd=fd)
            os.close(fd)
            fd = next_fd
        return fd
    except BaseException:
        os.close(fd)
        raise


def occupied(directory, name):
    try:
        os.stat(name, dir_fd=directory, follow_symlinks=False)
        return True
    except FileNotFoundError:
        return False


def write_batch(directory, outputs):
    created = []
    try:
        for name, body in outputs:
            fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o666, dir_fd=directory)
            identity = os.fstat(fd)
            created.append((name, identity.st_dev, identity.st_ino))
            with os.fdopen(fd, "wb") as stream:
                stream.write(body)
    except BaseException as error:
        cleanup_problems = []
        for name, device, inode in reversed(created):
            try:
                current = os.stat(name, dir_fd=directory, follow_symlinks=False)
                if (current.st_dev, current.st_ino) == (device, inode) and stat.S_ISREG(current.st_mode):
                    os.unlink(name, dir_fd=directory)
                else:
                    cleanup_problems.append(name + " changed identity; preserved")
            except FileNotFoundError:
                pass
            except OSError as cleanup_error:
                cleanup_problems.append(name + ": " + str(cleanup_error))
        print("Export failed: " + str(error), file=sys.stderr)
        if cleanup_problems:
            print("Inspect remaining state: " + "; ".join(cleanup_problems), file=sys.stderr)
        else:
            print("Created files rolled back; inspect state before retrying.", file=sys.stderr)
        return 4
    print(json.dumps({"created": [name for name, _ in outputs]}, ensure_ascii=True))
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="UTF-8 catalogue JSON file")
    parser.add_argument("--destination", required=True, help="Existing authorized directory")
    args = parser.parse_args()
    try:
        outputs = render(args.input)
        directory = open_destination(args.destination)
    except (OSError, ValueError, UnicodeError, RecursionError) as error:
        print("Stopped before output writes: " + str(error), file=sys.stderr)
        return 2
    try:
        conflicts = [name for name, _ in outputs if occupied(directory, name)]
        if conflicts:
            print("No outputs created. Occupied targets: " + ", ".join(conflicts)
                  + ". Ask for replacement permission or another destination.", file=sys.stderr)
            return 3
        return write_batch(directory, outputs)
    except OSError as error:
        print("Preflight failed before output writes: " + str(error), file=sys.stderr)
        return 2
    finally:
        os.close(directory)


if __name__ == "__main__":
    sys.exit(main())
