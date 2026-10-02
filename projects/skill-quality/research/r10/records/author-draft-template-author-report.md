# Author report: release-brief-update

## Deliverable

Package: package/release-brief-update/
- SKILL.md: authority gates, current-file repeat workflow, evidence/supersession handling, source citations, stage/count distinctions, checks and truthful reporting.
- scripts/replace_sections.py: standard-library, fail-closed atomic section-body replacement with exact preservation of protected bytes and stale-digest checks.

Development harness: test_development.py (outside package). Planned outputs: test-output/results.json, per-check local fixtures, original development bytes and expected draft. actions.md contains attributed actual actions, not a host trace.

## Assumptions and limits

The supplied brief explicitly authorizes replacing Summary and Schedule in dev-draft.md. D1 is a synthetic source; its explicit supersession controls the trial count/date. General release remains undecided. Notes is outside scope even if it appears outdated. Runtime users must independently supply their own authority; example flags do not grant it.

The helper deliberately accepts a conservative ATX-heading grammar and rejects ambiguous unsupported cases. It verifies scope and byte preservation, not source truth or whether the caller's permission assertions are genuine. Source-grounding review remains the consuming agent's responsibility. It avoids ordinary stale-file overwrites but is not a locking primitive; concurrent writers are unsupported. No network, publication, or installation is part of the package.

## Checks

Both generated Python files received coordinator safety review before their first execution; the repaired harness received renewed review before the second execution.

- Attempt 1: python3 test_development.py exited 1. Thirteen checks passed; one failed because the expected-byte oracle stripped a leading blank line present in its proposed replacement. The development draft remained unchanged. The original executable and every fixture/result from that attempt are retained in test_development_attempt1.py and test-output-attempt1/ (also test-output/results-attempt1.json).
- One autonomous test-harness repair: replacement bodies now match the draft's existing whitespace style; expected bytes use the complete replacement body. The packaged helper did not change.
- Attempt 2: python3 test_development.py exited 0. All 15 checks passed, including nine expected denied updates that preserved the entire draft, the supplied D1 result, repeat use of an actual preceding result, CRLF/absent-final-newline preservation, nested headings, and closed fenced content. The authorized development file was then updated and reread against expected bytes.
- Final manual inspection of the development output confirms the trial is approved for three sites on 2026-11-06, general release remains undecided, and each changed claim has [D1] attribution. Title, heading order, and protected Notes remain unchanged. No semantic claim verifier is implied by the byte tests.
- Unrun: CLI argument-path integration, duplicate JSON-key handling via CLI, symlink handling, injected concurrent-writer races, comprehensive CommonMark compatibility, and external evaluation. No supplied automated check suite existed; the tests described here were authored locally from the permitted brief/development inputs.

Current development-file SHA-256: b2e56767cad35f8f205f1c67ceaaa9ec4f58f4a87d8963da62ef6fe41e03e832.

## Timing

Admission approximately 2026-10-02 21:26:21 UTC; coordinator supplied the conservative stop of 21:36:10 UTC. Second run completed at approximately 21:34:23 UTC, 8 minutes 2 seconds after the first observed admission timestamp. Final inspection completed approximately 21:35:34 UTC. Sixteen top-level tool calls including final documentation (nested tools not double-counted); two actual test-script runs, one failed check, one harness repair, zero packaged-helper repairs. These are self-reported counts, not a complete host trace.
