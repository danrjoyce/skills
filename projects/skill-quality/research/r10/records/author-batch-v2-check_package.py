#!/usr/bin/env python3
"""Retained local tests; does not install, publish, use network, or remove fixtures."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "package/catalogue-export/scripts/export_catalogue.py"
RUN = Path(tempfile.mkdtemp(prefix="run-", dir=ROOT / "tests"))
RECORDS = []


def snapshot(path):
    result = {}
    for item in sorted(path.rglob("*")):
        name = str(item.relative_to(path))
        if item.is_symlink():
            result[name] = ["symlink", os.readlink(item)]
        elif item.is_file():
            result[name] = ["file", item.read_bytes().hex()]
        elif item.is_dir():
            result[name] = ["directory"]
    return result


def case(name, raw=None, occupied=None, code=0, expected=None, dest_link=False):
    folder = RUN / name
    folder.mkdir()
    destination = folder / "out"
    destination.mkdir()
    (destination / "protected.bin").write_bytes(b"protected\x00\xff\n")
    source = folder / "input.json"
    source.write_text(raw if raw is not None else (ROOT / "dev-input.json").read_text(encoding="utf-8"), encoding="utf-8")
    if occupied == "card":
        (destination / "amber.md").write_bytes(b"already here\x00")
    elif occupied == "index":
        (destination / "index.json").mkdir()
    elif occupied == "dangling":
        (destination / "amber.md").symlink_to(folder / "missing.md")
    actual_destination = destination
    if dest_link:
        actual_destination = folder / "alias"
        actual_destination.symlink_to(destination, target_is_directory=True)
    before = snapshot(folder)
    command = [sys.executable, str(SCRIPT), "--input", str(source), "--destination", str(actual_destination)]
    run = subprocess.run(command, text=True, capture_output=True)
    checks = {"exit": run.returncode == code,
              "protected": (destination / "protected.bin").read_bytes() == b"protected\x00\xff\n"}
    if code:
        checks["unchanged"] = before == snapshot(folder)
    if expected is not None:
        checks["only_expected"] = set(p.name for p in destination.iterdir()) == set(expected) | {"protected.bin"}
        for filename, content in expected.items():
            target = destination / filename
            checks[filename] = target.exists() and (json.loads(target.read_text(encoding="utf-8")) == content if filename == "index.json" else target.read_bytes() == content.encode("utf-8"))
    record = {"case": name, "command": command, "returncode": run.returncode,
              "stdout": run.stdout, "stderr": run.stderr, "checks": checks,
              "passed": all(checks.values())}
    RECORDS.append(record)
    (RUN / "results.json").write_text(json.dumps(RECORDS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, ensure_ascii=True), flush=True)


case("development", expected=json.loads((ROOT / "dev-expected.json").read_text(encoding="utf-8")))
case("occupied-card", occupied="card", code=3)
case("occupied-index-directory", occupied="index", code=3)
case("dangling-target-link", occupied="dangling", code=3)
case("destination-link", dest_link=True, code=2)
case("late-invalid-record", raw='[{"id":"amber","title":"Valid","tags":[]},{"id":"bad/id","title":"Invalid","tags":[]}]', code=2)
case("duplicate-id", raw='[{"id":"x","title":"X","tags":[]},{"id":"x","title":"Y","tags":[]}]', code=2)
case("extra-key", raw='[{"id":"x","title":"X","tags":[],"extra":1}]', code=2)
case("multiline-title", raw='[{"id":"x","title":"X\\nY","tags":[]}]', code=2)
case("nonstring-tag", raw='[{"id":"x","title":"X","tags":[1]}]', code=2)
case("duplicate-json-key", raw='[{"id":"x","id":"y","title":"X","tags":[]}]', code=2)
case("invalid-utf8-scalar", raw='[{"id":"x","title":"\\ud800","tags":[]}]', code=2)
case("empty", raw='[]', expected={"index.json": []})
case("changed-batch", raw=json.dumps([
    {"id":"z-2","title":"Café","tags":[" Zebra ","ÁRBOL","zebra","  ","β"]},
    {"id":"a","title":"A","tags":[]}
], ensure_ascii=False), expected={
    "a.md":"# A\n\nTags: (none)\n",
    "z-2.md":"# Café\n\nTags: zebra, árbol, β\n",
    "index.json":[{"id":"a","title":"A","tags":[],"file":"a.md"},
                  {"id":"z-2","title":"Café","tags":["zebra","árbol","β"],"file":"z-2.md"}]
})
print("RESULTS " + str(RUN / "results.json"))
print(f"TOTAL {len(RECORDS)}; PASSED {sum(r['passed'] for r in RECORDS)}; FAILED {sum(not r['passed'] for r in RECORDS)}")
sys.exit(0 if all(record["passed"] for record in RECORDS) else 1)
