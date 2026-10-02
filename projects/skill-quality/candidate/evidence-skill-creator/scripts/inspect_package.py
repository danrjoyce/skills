#!/usr/bin/env python3
"""Read-only limited package audit. Never imports or executes package code.

Python 3.10+. Exit 0: no detected defect; 1: defects; 2: incomplete audit.
This is not a general YAML/Markdown parser, host validator or security scanner.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

MAX_FILES = 1000
MAX_FILE_BYTES = 1_000_000
MAX_TOTAL_BYTES = 8_000_000
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def scalar(value):
    """Recognize a safe scalar subset; defer other YAML syntax, never guess."""
    value = value.strip()
    if value.startswith('"'):
        result = json.loads(value)
        if not isinstance(result, str):
            raise ValueError("not a string")
        return result
    if value.startswith("'") and re.fullmatch(r"'(?:[^']|'')*'", value):
        return value[1:-1].replace("''", "'")
    if not value or value[0] in "|>{[&*!%@`'0123456789+-." or ": " in value or "#" in value:
        raise ValueError("requires a full YAML parser")
    if value.lower() in {"null", "~", "true", "false", "yes", "no", "on", "off"}:
        raise ValueError("not a string")
    return value


def inspect(root):
    root = Path(root).absolute()
    result = {"audit": "limited-static-v1", "files": [], "errors": [],
              "manual_checks": [], "limits": [
                  "No code execution, network, behavior or native-host validation.",
                  "Only single-line name/description scalars and inline local Markdown file links are checked.",
                  "Anchors, reference-style links, permissions, hostile code and complete YAML semantics need separate review."]}
    errors, manual = result["errors"], result["manual_checks"]
    if root.is_symlink() or not root.is_dir():
        errors.append("Package root must be an existing real directory.")
        return result
    root = root.resolve()
    texts = {}
    total = 0
    entries = 0
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs.sort()
        files.sort()
        for name in list(dirs) + files:
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            if path.is_symlink():
                errors.append(f"Symlink requires separate review: {rel}")
                if name in dirs:
                    dirs.remove(name)
                continue
            if path.is_dir():
                continue
            if not path.is_file():
                errors.append(f"Non-regular file: {rel}")
                continue
            entries += 1
            size = path.stat().st_size
            total += size
            if entries > MAX_FILES or size > MAX_FILE_BYTES or total > MAX_TOTAL_BYTES:
                manual.append(f"Audit size limit reached at {rel}; incomplete inventory.")
                result["inventory_complete"] = False
                return result
            data = path.read_bytes()
            result["files"].append({"path": rel, "bytes": len(data),
                                    "sha256": hashlib.sha256(data).hexdigest()})
            if path.suffix.lower() == ".md":
                try:
                    texts[rel] = data.decode("utf-8")
                except UnicodeDecodeError:
                    errors.append(f"Markdown is not UTF-8: {rel}")
    result["files"].sort(key=lambda item: item["path"])
    result["inventory_complete"] = True
    main = texts.get("SKILL.md", "")
    if not main.startswith("---\n") or "\n---\n" not in main[4:]:
        errors.append("SKILL.md needs delimited YAML frontmatter and a body.")
    else:
        front, body = main[4:].split("\n---\n", 1)
        if not body.strip():
            errors.append("SKILL.md body is empty.")
        for key in ("name", "description"):
            matches = list(re.finditer(rf"^{key}:[ \t]*([^\n]*)$", front, re.M))
            if len(matches) != 1:
                errors.append(f"Expected one top-level {key} field.")
                continue
            try:
                following = next((line for line in front[matches[0].end():].splitlines()
                                  if line.strip() and not line.lstrip().startswith("#")), "")
                if following.startswith((" ", "\t")):
                    raise ValueError("multiline value requires a full YAML parser")
                value = scalar(matches[0].group(1))
            except (ValueError, json.JSONDecodeError):
                manual.append(f"Check {key} with the target YAML parser.")
                continue
            if not value.strip():
                errors.append(f"Empty {key}.")
            if key == "name" and (not NAME.fullmatch(value) or len(value) > 64 or value != root.name):
                errors.append("Name must match the directory and the lowercase hyphenated 1-64 character profile.")
            if key == "description" and len(value) > 1024:
                errors.append("Description exceeds 1024 characters.")
    for rel, content in sorted(texts.items()):
        for target in LINK.findall(content):
            parts = urlsplit(target.strip("<>"))
            if parts.scheme or parts.netloc or not parts.path:
                continue
            dest = root / Path(rel).parent / unquote(parts.path)
            resolved = dest.resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"Local link leaves package: {rel}: {target}")
            elif not resolved.is_file():
                errors.append(f"Local file link missing: {rel}: {target}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    args = parser.parse_args()
    try:
        report = inspect(args.package)
    except (OSError, ValueError) as exc:
        print(json.dumps({"audit": "limited-static-v1", "error": str(exc),
                          "inventory_complete": False}))
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["errors"] else (2 if report["manual_checks"] else 0)


if __name__ == "__main__":
    raise SystemExit(main())
