#!/usr/bin/env python3
"""Preflight and exclusively create a local catalogue export. Python stdlib only."""
import argparse
import json
import os
import re
import sys


class ExportError(Exception):
    pass


LINE_BREAKS = frozenset("\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029")
ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ExportError("Duplicate JSON object key: " + repr(key))
        result[key] = value
    return result


def reject_constant(value):
    raise ExportError("Invalid JSON constant: " + value)


def single_line(value):
    return isinstance(value, str) and not any(c in LINE_BREAKS for c in value)


def prepare(input_path):
    with open(input_path, "r", encoding="utf-8", errors="strict") as source:
        rows = json.load(source, object_pairs_hook=unique_object,
                         parse_constant=reject_constant)
    if not isinstance(rows, list):
        raise ExportError("Input must be a JSON array.")
    seen = set()
    normalized = []
    for number, row in enumerate(rows, 1):
        prefix = "Record " + str(number) + ": "
        if not isinstance(row, dict) or set(row) != {"id", "title", "tags"}:
            raise ExportError(prefix + "expected exactly id, title, and tags.")
        identifier, title, tags = row["id"], row["title"], row["tags"]
        if not isinstance(identifier, str) or ID_RE.fullmatch(identifier) is None:
            raise ExportError(prefix + "invalid ID.")
        if identifier in seen:
            raise ExportError(prefix + "duplicate ID " + repr(identifier) + ".")
        seen.add(identifier)
        if not single_line(title) or title == "":
            raise ExportError(prefix + "title must be a nonempty single line.")
        if not isinstance(tags, list) or not all(single_line(tag) for tag in tags):
            raise ExportError(prefix + "tags must be an array of single-line strings.")
        tags = sorted({tag.strip().lower() for tag in tags} - {""})
        normalized.append({"id": identifier, "title": title,
                           "tags": tags, "file": identifier + ".md"})
    normalized.sort(key=lambda row: row["id"])
    outputs = []
    for row in normalized:
        card = "# " + row["title"] + "\n\nTags: " + (", ".join(row["tags"]) or "(none)") + "\n"
        outputs.append((row["file"], card.encode("utf-8", errors="strict")))
    index = json.dumps(normalized, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    outputs.append(("index.json", index.encode("utf-8", errors="strict")))
    return outputs


def open_destination(destination):
    if os.name != "posix" or not hasattr(os, "O_NOFOLLOW") or not hasattr(os, "O_DIRECTORY"):
        raise ExportError("POSIX directory descriptors and O_NOFOLLOW are required.")
    if ".." in destination.split(os.sep):
        raise ExportError("Destination may not contain '..' components.")
    absolute = os.path.abspath(destination)
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    fd = os.open(os.sep, flags)
    try:
        for component in absolute.split(os.sep):
            if component:
                next_fd = os.open(component, flags, dir_fd=fd)
                os.close(fd)
                fd = next_fd
        return fd
    except BaseException:
        os.close(fd)
        raise


def export(outputs, destination):
    directory_fd = open_destination(destination)
    created = []
    try:
        occupied = []
        for name, _ in outputs:
            try:
                os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
            except FileNotFoundError:
                pass
            else:
                occupied.append(name)
        if occupied:
            raise ExportError("No outputs created. Occupied targets: " +
                              ", ".join(occupied) +
                              ". Ask for permission before replacing them.")
        try:
            for name, content in outputs:
                fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                             0o666, dir_fd=directory_fd)
                try:
                    stat = os.fstat(fd)
                    created.append((name, stat.st_dev, stat.st_ino))
                    with os.fdopen(fd, "wb") as target:
                        fd = None
                        target.write(content)
                finally:
                    if fd is not None:
                        os.close(fd)
        except BaseException as error:
            rollback_failures = []
            for name, device, inode in reversed(created):
                try:
                    stat = os.stat(name, dir_fd=directory_fd, follow_symlinks=False)
                    if (stat.st_dev, stat.st_ino) == (device, inode):
                        os.unlink(name, dir_fd=directory_fd)
                    else:
                        rollback_failures.append(name + " (replaced concurrently)")
                except FileNotFoundError:
                    pass
                except OSError as cleanup_error:
                    rollback_failures.append(name + " (" + str(cleanup_error) + ")")
            if rollback_failures:
                raise ExportError("Export failed: " + str(error) +
                                  "; rollback incomplete: " + ", ".join(rollback_failures)) from error
            raise
    finally:
        os.close(directory_fd)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="UTF-8 JSON input file")
    parser.add_argument("--destination", required=True, help="Existing authorized directory")
    args = parser.parse_args()
    try:
        outputs = prepare(args.input)
        export(outputs, args.destination)
    except (ExportError, OSError, ValueError, RecursionError) as error:
        print("Export stopped: " + str(error), file=sys.stderr)
        return 1
    print("Exported " + str(len(outputs) - 1) + " cards and index.json to " + args.destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
