"""Local author checks; writes only assigned development and test-output files."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("replace_sections", ROOT / "package/release-brief-update/scripts/replace_sections.py")
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
OUT = ROOT / "test-output"
OUT.mkdir(exist_ok=True)
original = (ROOT / "dev-draft.md").read_bytes()
(OUT / "original-draft.bin").write_bytes(original)
updates = {
    "Summary": "\nTrial approved for three sites. [D1]\nGeneral release remains undecided. [D1]\n\n",
    "Schedule": "\nTrial approved for 2026-11-06. [D1]\n\n",
}
allowed = ["Summary", "Schedule"]
digest = lambda data: hashlib.sha256(data).hexdigest()
passed = []
failed = []


def check(name, operation):
    try:
        operation()
        passed.append(name)
        print("PASS " + name)
    except Exception as exc:
        failed.append({"test": name, "error": repr(exc)})
        print("FAIL " + name + ": " + repr(exc))


def equal(actual, expected):
    assert actual == expected, (actual, expected)


def reject(name, data=original, proposed=updates, authority=allowed, permission=True, sha=None):
    path = OUT / (name + ".md")
    path.write_bytes(data)
    try:
        helper.apply_update(path, proposed, authority, permission, sha or digest(data))
    except helper.UpdateError as exc:
        equal(path.read_bytes(), data)
        print("  Expected rejection: " + str(exc))
    else:
        raise AssertionError("Expected rejection, but update was accepted")


def development_plan():
    expected = original.replace(b"Draft for two sites.\n\n", updates["Summary"].encode()[1:]).replace(b"Trial planned 2026-11-04.\n\n", updates["Schedule"].encode()[1:])
    result = helper.plan_update(original, updates, allowed, True, digest(original))
    equal(result, expected)
    equal(result[result.index(b"## Notes"):], original[original.index(b"## Notes"):])
    (OUT / "expected-draft.md").write_bytes(expected)


def repeat_update():
    path = OUT / "repeat.md"
    path.write_bytes(original)
    first = helper.apply_update(path, updates, allowed, True, digest(original))
    current = path.read_bytes()
    second_body = "\nGeneral release remains undecided. [D1]\nTrial approved for three sites. [D1]\n\n"
    helper.apply_update(path, {"Summary": second_body}, ["Summary"], True, digest(current))
    equal(path.read_bytes(), current.replace(updates["Summary"].encode(), second_body.encode()))
    equal(path.read_bytes()[path.read_bytes().index(b"## Schedule"):], current[current.index(b"## Schedule"):])
    report = helper.apply_update(path, {"Summary": second_body}, ["Summary"], True, digest(path.read_bytes()))
    equal(report["changed"], False)
    assert first["changed"]


def crlf_and_final_newline():
    data = original.replace(b"\n", b"\r\n").rstrip(b"\r\n")
    crlf_updates = {key: val.replace("\n", "\r\n") for key, val in updates.items()}
    result = helper.plan_update(data, crlf_updates, allowed, True, digest(data))
    equal(result[result.index(b"## Notes"):], data[data.index(b"## Notes"):])
    assert not result.endswith(b"\n")
    assert b"\n" not in result.replace(b"\r\n", b"")


def nested_heading():
    data = original.replace(b"Draft for two sites.\n\n", b"Draft for two sites.\n\n### Protected detail\nStale-looking fact.\n\n")
    result = helper.plan_update(data, {"Summary": updates["Summary"]}, ["Summary"], True, digest(data))
    equal(result[result.index(b"### Protected detail"):], data[data.index(b"### Protected detail"):])


def fenced_heading():
    data = original + b"\n```text\n## Not a section\n```\n"
    result = helper.plan_update(data, updates, allowed, True, digest(data))
    equal(result[result.index(b"## Notes"):], data[data.index(b"## Notes"):])


check("D1 facts and exact expected bytes", development_plan)
check("missing replacement permission leaves all bytes unchanged", lambda: reject("missing-permission", permission=False))
check("mixed unauthorized request leaves all bytes unchanged", lambda: reject("mixed-scope", proposed={**updates, "Notes": "\nOverwritten\n"}))
check("missing section leaves all bytes unchanged", lambda: reject("missing-section", proposed={"Absent": "\nText\n"}, authority=["Absent"]))
check("new heading in body leaves all bytes unchanged", lambda: reject("new-heading", proposed={"Summary": "\n## New section\nText\n"}))
check("stale digest leaves all bytes unchanged", lambda: reject("stale", sha="0" * 64))
check("title protected even if named in authority", lambda: reject("title", proposed={"Demo release brief": "changed\n"}, authority=["Demo release brief"]))
check("duplicate headings refused unchanged", lambda: reject("duplicates", data=original + b"\n## Summary\nDuplicate\n"))
check("setext boundary ambiguity refused unchanged", lambda: reject("setext", data=original + b"\nHeading\n-------\n"))
check("unclosed fence refused unchanged", lambda: reject("fence", data=original + b"\n```\n"))
check("repeat use preserves actual preceding result", repeat_update)
check("CRLF and absent final newline preserved outside scope", crlf_and_final_newline)
check("nested heading and its body stay protected", nested_heading)
check("heading-like text inside closed fence stays protected", fenced_heading)

if not failed:
    report = helper.apply_update(ROOT / "dev-draft.md", updates, allowed, True, digest(original))
    check("authorized development file updated and reread", lambda: equal((ROOT / "dev-draft.md").read_bytes(), (OUT / "expected-draft.md").read_bytes()))
    print("Development write: " + json.dumps(report))
results = {"passed": passed, "failed": failed, "checks": len(passed) + len(failed), "expected_rejections": 9}
(OUT / "results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results))
sys.exit(1 if failed else 0)
