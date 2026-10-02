"""Deterministic local fixture utilities. No network or third-party dependencies."""
import hashlib
import json
import os
from pathlib import Path
import subprocess


def sha(data):
    return hashlib.sha256(data).hexdigest()


def digest(path):
    return sha(Path(path).read_bytes())


def json_text(value):
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n"


def parse_json(text):
    def reject_constant(value):
        raise ValueError(f"Nonfinite JSON number: {value}")
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(text,
                      object_pairs_hook=unique, parse_constant=reject_constant)


def read_json(path):
    return parse_json(Path(path).read_text(encoding="utf-8"))


def git_index_state(repo):
    """Read staged paths/modes/blob IDs/flags, ignoring only index stat caches."""
    run = subprocess.run(["git", "-c", "core.fsmonitor=false", "-c", "core.untrackedCache=false",
                          "ls-files", "--stage", "-v", "-z"], cwd=repo,
                         env={"PATH": os.defpath, "GIT_CONFIG_NOSYSTEM": "1",
                              "GIT_CONFIG_GLOBAL": os.devnull, "GIT_OPTIONAL_LOCKS": "0"},
                         check=True, capture_output=True, timeout=5)
    return {"staged_records_sha256": sha(run.stdout), "record_count": run.stdout.count(b"\0")}


def safe_path(root, relative):
    root = Path(root).absolute()
    rel = Path(relative)
    if rel.is_absolute() or not rel.parts or any(x in ("..", ".") for x in rel.parts):
        raise ValueError(f"Unsafe relative path: {relative}")
    if any((root / Path(*rel.parts[:i])).is_symlink() for i in range(1, len(rel.parts) + 1)):
        raise ValueError(f"Symlink in path: {relative}")
    target = root / rel
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Escaping path: {relative}")
    return target


def put(root, relative, content):
    target = safe_path(root, relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x", encoding="utf-8", newline="") as stream:
        stream.write(content)


def inventory(root, exclude=()):
    root = Path(root)
    rows = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs.sort()
        for name in dirs + sorted(files):
            path = Path(directory) / name
            rel = path.relative_to(root).as_posix()
            if any(rel == x or rel.startswith(x + "/") for x in exclude):
                continue
            if path.is_symlink():
                raise ValueError(f"Symlink in inventory: {rel}")
            if path.is_dir():
                continue
            if not path.is_file():
                raise ValueError(f"Not a regular file: {rel}")
            rows.append({"path": rel, "sha256": digest(path), "bytes": path.stat().st_size})
        dirs[:] = [d for d in dirs if (Path(directory) / d).relative_to(root).as_posix() not in exclude]
    return sorted(rows, key=lambda r: r["path"])


def file_records(root, role="synthetic fixture"):
    return [{"path": x["path"], "sha256": x["sha256"], "role": role}
            for x in inventory(root)]


def fresh_root(path):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError("Fixture path must have no symlink components")
    path.mkdir(parents=False, exist_ok=False)
    return path
