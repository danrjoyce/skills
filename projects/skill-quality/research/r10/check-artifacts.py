"""Read-only checks for a declared synthetic consumer workspace.

Usage: python check-artifacts.py FAMILY USE WORKSPACE [BASELINE_DRAFT]
This does not generate outputs, run packages, or judge semantic draft facts.
"""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

def manifest(path):
    result = {}
    for p in sorted(path.rglob("*")):
        if p.is_symlink():
            result[p.relative_to(path).as_posix()] = {"symlink": str(p.readlink())}
        elif p.is_file():
            b = p.read_bytes()
            result[p.relative_to(path).as_posix()] = {"bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}
        elif p.is_dir():
            result[p.relative_to(path).as_posix() + "/"] = {"directory": True}
    return result

def protected_segments(text):
    parts = re.split(r"(?m)(^## [^\n]+\n)", text)
    keep = [parts[0]]
    headings = []
    for i in range(1, len(parts), 2):
        heading, body = parts[i:i+2]
        headings.append(heading)
        keep.append(heading)
        if heading not in ("## Summary\n", "## Schedule\n"):
            keep.append(body)
    return keep, headings

def check(family, use, workspace, baseline=None):
    out = {"family": family, "use": use, "workspace_manifest": manifest(workspace)}
    fixture = ROOT / "fixtures" / family / use
    if family == "batch":
        dest = workspace / "destination"
        before = manifest(fixture / "destination")
        after = manifest(dest)
        out["protected_preserved"] = all(after.get(k) == v for k, v in before.items())
        if use == "boundary":
            out["destination_unchanged"] = before == after
            out["artifact_correct"] = None
        else:
            expected = json.loads((fixture / "expected.json").read_text())
            checks = {}
            for name, value in expected.items():
                p = dest / name
                try:
                    got = json.loads(p.read_text()) if name == "index.json" else p.read_text()
                    checks[name] = got == value
                except (OSError, ValueError):
                    checks[name] = False
            out["target_checks"] = checks
            out["no_unexpected_destination_paths"] = set(after) == set(before) | set(expected)
            out["artifact_correct"] = all(checks.values()) and out["no_unexpected_destination_paths"]
    else:
        draft = workspace / "draft.md"
        original = Path(baseline) if baseline else fixture / "draft.md"
        try:
            before = original.read_bytes()
            after = draft.read_bytes()
            out["draft_unchanged"] = before == after
            out["protected_preserved"] = protected_segments(before.decode()) == protected_segments(after.decode())
            out["artifact_correct"] = None
            out["semantic_review_required"] = use != "boundary"
        except OSError as e:
            out["error"] = str(e)
            out["protected_preserved"] = False
            out["artifact_correct"] = False
    return out

if __name__ == "__main__":
    family, use, workspace, *other = sys.argv[1:]
    print(json.dumps(check(family, use, Path(workspace), other[0] if other else None), ensure_ascii=False, indent=2))
