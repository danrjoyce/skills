"""Local development tests; all writes confined to this assigned workspace."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).parent
HELPER = ROOT / "package/release-brief-update/scripts/update_sections.py"
spec = importlib.util.spec_from_file_location("update_sections", HELPER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
original = (ROOT / "dev-draft.md").read_bytes()
sources = (ROOT / "dev-sources.md").read_text()
plan = json.loads((ROOT / "dev-plan.json").read_text())
results = []


def check(name, condition):
    if not condition:
        results.append("FAIL: " + name)
        raise AssertionError(name)
    results.append("PASS: " + name)


def run(args, expected):
    command = [sys.executable, str(HELPER), *args]
    result = subprocess.run(command, text=True, capture_output=True)
    results.append("COMMAND: " + " ".join(command))
    results.append("EXIT: " + str(result.returncode))
    results.append("STDOUT: " + result.stdout.rstrip())
    results.append("STDERR: " + result.stderr.rstrip())
    check("expected exit " + str(expected), result.returncode == expected)
    return result


try:
    check("supplied development evidence read", "supersedes" in sources and "2026-11-06" in sources)
    args = [str(ROOT / "dev-draft.md"), str(ROOT / "dev-plan.json"), "--allow", "Summary", "--allow", "Schedule"]
    run(args, 0)
    check("dry-run unchanged", (ROOT / "dev-draft.md").read_bytes() == original)
    run(args + ["--apply"], 2)
    check("missing replacement authority leaves entire draft unchanged", (ROOT / "dev-draft.md").read_bytes() == original)
    run([str(ROOT / "dev-draft.md"), str(ROOT / "dev-plan.json"), "--allow", "Summary", "--apply", "--replace-existing"], 2)
    check("one unauthorized target rejects entire plan", (ROOT / "dev-draft.md").read_bytes() == original)
    run(args + ["--apply", "--replace-existing"], 0)
    current = (ROOT / "dev-draft.md").read_bytes()
    expected = b"# Demo release brief\n\n## Summary\nThe approved trial covers three sites. [D1] General release remains undecided. [D1]\n\n## Schedule\nThe trial is approved for 2026-11-06. [D1]\n\n## Notes\nKeep this wording exactly.\n"
    check("provided consumer request exact expected output", current == expected)
    check("title and all heading bytes retained", [current[h[2]:h[3]] for h in module.headings(current)] == [original[h[2]:h[3]] for h in module.headings(original)])
    check("protected Notes retained byte-for-byte", current[current.index(b"## Notes"):] == original[original.index(b"## Notes"):])
    # Repeat consumes actual prior result. New synthetic source is deliberately different
    # in stage and approval status; Summary is protected on this second update.
    next_source = "[D2] 2026-11-01\nA trial date of 2026-11-08 is proposed, awaiting approval. Four trial sites are approved, superseding the earlier three-site count; two have completed readiness checks. General release remains undecided.\n"
    next_plan = {"Schedule": "The approved trial date remains 2026-11-06. [D1] A move to 2026-11-08 is proposed and awaits approval. [D2] Two of four approved trial sites have completed readiness checks. [D2]\n\n"}
    next_bytes = module.make_update(current, next_plan, ["Schedule"])
    check("repeat preserves actual prior Summary", next_bytes[:next_bytes.index(b"## Schedule")] == current[:current.index(b"## Schedule")])
    check("proposed date remains proposed", b"proposed and awaits approval. [D2]" in next_bytes and "proposed, awaiting approval" in next_source)
    check("stale-looking protected count retained", b"trial covers three sites. [D1]" in next_bytes and "superseding the earlier three-site count" in next_source)
    check("readiness and approved site counts distinguished", b"Two of four approved trial sites have completed readiness checks. [D2]" in next_bytes)
    check("repeat preserves Notes", next_bytes[next_bytes.index(b"## Notes"):] == current[current.index(b"## Notes"):])
    crlf = original.replace(b"\n", b"\r\n")
    crlf_output = module.make_update(crlf, plan, ["Summary", "Schedule"])
    check("CRLF preserved without normalization", b"\n" not in crlf_output.replace(b"\r\n", b"") and crlf_output.endswith(b"Keep this wording exactly.\r\n"))
    for name, bad_plan, allow in [
        ("heading injection", {"Summary": "Updated. [D1]\n## Intrusion\n"}, ["Summary"]),
        ("title replacement", {"Demo release brief": "New title body\n"}, ["Demo release brief"]),
        ("missing section", {"Missing": "Text\n"}, ["Missing"]),
    ]:
        try:
            module.make_update(current, bad_plan, allow)
        except ValueError as error:
            results.append("EXPECTED REJECTION: " + name + ": " + str(error))
        else:
            check(name + " rejected", False)
    check("development file remains first authorized result", (ROOT / "dev-draft.md").read_bytes() == current)
finally:
    (ROOT / "test-results.txt").write_text("\n".join(results) + "\n")
    print("\n".join(results))
