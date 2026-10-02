# Author report: catalogue-export

Package: `package/catalogue-export/`.

## Deliverable and assumptions

Created a reusable skill and Python standard-library exporter because the repeated normalization, exact formatting, whole-batch validation, collision checks, and symlink containment benefit from one deterministic implementation. It uses consumer-provided input/destination paths and has no hardcoded development values. Authorization is restricted to local creation in an existing destination, with no overwrite authority.

Files:
- `SKILL.md`: trigger, input/output contract, usage, safety behavior, tools, and limitations.
- `scripts/export_catalogue.py`: strict batch validation, exact card bytes, sorted index, symlink-safe directory walk, preflight, exclusive creation, and guarded rollback of new files.
- `tests/check_export.py`: repeatable example and safety checks in a fresh explicitly supplied workspace.

Assumptions: POSIX Python supports O_NOFOLLOW and directory-descriptor operations. The destination is stable during execution. All destination symlinks are conservatively rejected, including internal symlinks; literal `..` path components are rejected. Unicode line separators are treated as line breaks. Whitespace-only titles remain valid nonempty strings. Inputs that cannot be emitted as valid UTF-8 are malformed.

## Actual checks and limitations

Final state: package complete. Coordinator reviewed and approved the current executable bytes at approximately 21:23:12 UTC. The approved test command completed at approximately 21:23:21 UTC, exit code 0. All 24 cases passed on the first suite invocation: 24 exporter subprocess attempts, 24 passed checks, 0 failures, 0 repairs, and 0 reruns. Including the runner, 25 generated-script executions occurred. The test runner measured 0.607 seconds for its case execution window.

Passed checks cover the provided example's exact card bytes and parsed index, changed data/destination, Unicode normalization and sort order, empty input, unrelated-byte preservation, exact-target file/directory/dangling-symlink conflicts, final and parent destination symlinks, malformed JSON/UTF-8/schema/values/IDs, a later invalid record, and duplicate JSON keys. All negative cases returned a clear error and preserved the recorded fixture state. Full real subprocess commands, return codes, stdout, stderr, and assertions are retained in `test-run-1/run-log.jsonl`; aggregate results are in `test-run-1/summary.json`. All fixtures remain intact.

Unrun: induced late-write failures and rollback/deletion checks (outside the coordinator's execution approval); process-kill/crash recovery; simultaneous writers; huge inputs; Windows or non-POSIX execution. No claims are made that these passed.

Not designed as a crash-safe multi-file transaction. Hardware failures, killed processes, malicious concurrent writers, and unrecoverable rollback errors can leave partial outputs; diagnostics and skill instructions disclose this. Large catalogues are kept in memory. No installation, network, publishing, or writes outside the assignment workspace have occurred.

Admission approximately 21:16:55 UTC on 2026-10-02. Review requested at approximately 21:22:15 UTC. Coordinator supplied the conservative terminal deadline 21:26:44 UTC. Checks finished approximately 6 minutes 26 seconds after admission; final documentation completed before the deadline. Final self-reported outer tool-call count is 10: 8 functions calls and 2 collaboration calls. The functions calls each invoked one nested tool (4 exec_command and 4 apply_patch). If outer wrappers and nested invocations are counted separately, total is 18. This is an attributed record, not a complete host trace. No executable source was changed after review.
