#!/usr/bin/env python3
"""Exercise exporter in a fresh, explicitly supplied local test workspace."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def snapshot(directory):
    result = {}
    for entry in sorted(directory.iterdir()):
        if entry.is_symlink():
            result[entry.name] = ["symlink", os.readlink(entry)]
        elif entry.is_dir():
            result[entry.name] = ["directory", snapshot(entry)]
        else:
            result[entry.name] = ["file", entry.read_bytes().hex()]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument("--work", required=True)
    args = parser.parse_args()
    work = Path(args.work)
    work.mkdir(parents=False, exist_ok=False)
    script = Path(__file__).resolve().parents[1] / "scripts" / "export_catalogue.py"
    expected = json.loads(Path(args.expected).read_text(encoding="utf-8"))
    failures = []
    attempts = 0
    began = time.monotonic()

    def run_case(name, raw, expected_outputs=None, occupied=None, destination_kind=None):
        nonlocal attempts
        case = work / name
        case.mkdir()
        source = case / "input.json"
        source.write_bytes(raw)
        destination = case / "destination"
        outside = case / "outside"
        outside.mkdir()
        (outside / "protected.bin").write_bytes(b"outside\x00unchanged\xff")
        if destination_kind == "symlink":
            destination.symlink_to(outside, target_is_directory=True)
        elif destination_kind == "parent-symlink":
            (outside / "nested").mkdir()
            link = case / "linked-parent"
            link.symlink_to(outside, target_is_directory=True)
            destination = link / "nested"
        else:
            destination.mkdir()
            (destination / "unrelated.bin").write_bytes(b"protected\x00bytes\xff")
            if occupied:
                target, kind = occupied
                if kind == "directory":
                    (destination / target).mkdir()
                elif kind == "symlink":
                    (destination / target).symlink_to(outside / "missing")
                else:
                    (destination / target).write_bytes(b"do not replace\x00")
        before = snapshot(case)
        command = [sys.executable, str(script), "--input", str(source), "--destination", str(destination)]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=15)
        attempts += 1
        problem = None
        try:
            if expected_outputs is None:
                assert completed.returncode != 0, "invalid or occupied case succeeded"
                assert snapshot(case) == before, "failed export changed filesystem content"
                assert "Export stopped:" in completed.stderr, "missing clear stop diagnostic"
            else:
                assert completed.returncode == 0, completed.stderr
                expected_names = set(expected_outputs) | {"unrelated.bin"}
                assert {p.name for p in destination.iterdir()} == expected_names, "unexpected output names"
                for filename, value in expected_outputs.items():
                    path = destination / filename
                    if filename == "index.json":
                        assert json.loads(path.read_text(encoding="utf-8")) == value, "index mismatch"
                    else:
                        assert path.read_bytes() == value.encode("utf-8"), "card byte mismatch: " + filename
                assert (destination / "unrelated.bin").read_bytes() == b"protected\x00bytes\xff"
                assert snapshot(outside) == before["outside"][1], "outside file changed"
                assert source.read_bytes() == raw, "input changed"
        except AssertionError as error:
            problem = str(error)
            failures.append(name + ": " + problem)
        record = {"case": name, "command": command, "returncode": completed.returncode,
                  "stdout": completed.stdout, "stderr": completed.stderr,
                  "check": "FAIL" if problem else "PASS", "problem": problem}
        with (work / "run-log.jsonl").open("a", encoding="utf-8") as log:
            log.write(json.dumps(record, ensure_ascii=True) + "\n")
        print(name + ": " + record["check"])

    def encoded(rows):
        return json.dumps(rows, ensure_ascii=True).encode("utf-8")

    development = Path(args.input).read_bytes()
    run_case("development", development, expected)
    varied = [{"id": "z-last", "title": "Zebra café", "tags": [" Z ", "é", "A", "a", "  "]},
              {"id": "a-first", "title": "  First  ", "tags": []}]
    run_case("changed-data", encoded(varied), {
        "a-first.md": "#   First  \n\nTags: (none)\n",
        "z-last.md": "# Zebra café\n\nTags: a, z, é\n",
        "index.json": [{"id": "a-first", "title": "  First  ", "tags": [], "file": "a-first.md"},
                       {"id": "z-last", "title": "Zebra café", "tags": ["a", "z", "é"], "file": "z-last.md"}]})
    run_case("empty-batch", b"[]", {"index.json": []})
    for name, target, kind in [("occupied-card", "amber.md", "file"),
                               ("occupied-index", "index.json", "file"),
                               ("occupied-directory", "amber.md", "directory"),
                               ("dangling-target", "index.json", "symlink")]:
        run_case(name, development, occupied=(target, kind))
    run_case("destination-symlink", development, destination_kind="symlink")
    run_case("parent-symlink", development, destination_kind="parent-symlink")
    good = {"id": "ok", "title": "Valid", "tags": [" A "]}
    malformed = {
        "wrong-root": {},
        "extra-field": [dict(good, extra="x")],
        "missing-field": [{"id": "ok", "title": "Valid"}],
        "invalid-id": [dict(good, id="../escape")],
        "duplicate-id": [good, good],
        "empty-title": [dict(good, title="")],
        "title-newline": [dict(good, title="one\ntwo")],
        "tags-not-array": [dict(good, tags="A")],
        "tag-not-string": [dict(good, tags=[3])],
        "tag-newline": [dict(good, tags=["one\rtwo"])],
        "late-invalid-record": [good, dict(good, id="later", title="")],
        "invalid-unicode": [dict(good, title="\ud800")],
    }
    for name, rows in malformed.items():
        run_case(name, encoded(rows))
    run_case("invalid-utf8", b"[\xff]")
    run_case("invalid-json", b"[{broken]")
    run_case("duplicate-key", b'[{"id":"a","id":"b","title":"Title","tags":[]}]')
    summary = {"attempted_subprocess_runs": attempts, "passed": attempts - len(failures),
               "failed": len(failures), "failures": failures,
               "elapsed_seconds": round(time.monotonic() - began, 3)}
    (work / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
