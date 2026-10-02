#!/usr/bin/env python3
"""Read-only R8 package/freeze checks. Requires installed PyYAML; no model runs."""
import hashlib
import json
from pathlib import Path
import re

import yaml

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
PACKAGE = PROJECT / "candidate/evidence-skill-creator-v2"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def inventory(root):
    rows = []
    for path in sorted(root.rglob("*")):
        assert not path.is_symlink(), f"Unexpected symlink: {path}"
        if path.is_dir():
            continue
        assert path.is_file(), f"Unexpected non-file: {path}"
        data = path.read_bytes()
        rows.append({"path": path.relative_to(root).as_posix(),
                     "bytes": len(data), "sha256": sha(data)})
    return rows


def tree_sha(rows):
    return sha(json.dumps(rows, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False, allow_nan=False).encode())


def main():
    rows = inventory(PACKAGE)
    assert [r["path"] for r in rows] == ["SKILL.md", "agents/openai.yaml"]
    text = (PACKAGE / "SKILL.md").read_text()
    assert text.startswith("---\n")
    front, body = text[4:].split("\n---\n", 1)
    meta = yaml.safe_load(front)
    assert set(meta) == {"name", "description"}
    assert meta["name"] == PACKAGE.name and len(meta["name"]) <= 64
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["name"])
    assert isinstance(meta["description"], str) and 0 < len(meta["description"]) <= 1024
    assert body.strip()
    ui = yaml.safe_load((PACKAGE / "agents/openai.yaml").read_text())
    assert set(ui) == {"interface"}, "Preserve model/user invocation defaults"
    assert set(ui["interface"]) == {"display_name", "short_description"}
    assert all(isinstance(v, str) and v.strip() for v in ui["interface"].values())
    assert 25 <= len(ui["interface"]["short_description"]) <= 64
    assert "\u2014" not in text, "Repository prose excludes em dashes"
    freeze = json.loads((HERE / "candidate-freeze.json").read_text())
    assert rows == freeze["files"]
    assert tree_sha(rows) == freeze["tree_sha256"]
    assert len(text.split()) == freeze["entrypoint_whitespace_words"]
    old = PROJECT / "candidate/evidence-skill-creator"
    old_freeze = json.loads((HERE.parent / "r5/candidate-freeze.json").read_text())
    old_rows = inventory(old)
    assert old_rows == old_freeze["files"]
    assert tree_sha(old_rows) == old_freeze["tree_sha256"]
    assert len(text.split()) < len((old / "SKILL.md").read_text().split())
    print(json.dumps({"status": "passed", "scope": "static package and frozen byte identity",
                      "files": rows, "tree_sha256": tree_sha(rows),
                      "entrypoint_whitespace_words": len(text.split()),
                      "package_bytes": sum(r["bytes"] for r in rows),
                      "v1_tree_sha256": tree_sha(old_rows), "new_model_trials": 0,
                      "limits": ["Assertions check the chosen two-file package, not skill quality.",
                                 "No creator, helper, solver, semantic grader or native host is exercised.",
                                 "No safety, usefulness, cost or comparative-performance inference."]},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
