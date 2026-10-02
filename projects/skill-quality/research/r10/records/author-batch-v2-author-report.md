# catalogue-export author report

## Delivered

Research-only reusable package: `package/catalogue-export/`.

- `SKILL.md`: fresh-consumer input/output contract, invocation, collision permission boundary, symlink policy, failure handling, and verification.
- `scripts/export_catalogue.py`: Python-standard-library implementation, strict whole-batch preflight, UTF-8 rendering, ID/tag sorting, exact-target collision checks, anchored no-follow path access, and exclusive creation.

Development evidence remains outside the package: `check_package.py`, `actions.md`, and `tests/run-nvzp7kzm/results.json` with all fixtures and outputs. Only the assigned brief, supplied creator policy, development input/expectation, and this worker's own generated files were inspected. The package was not installed or published.

## Observed checks

After coordinator safety approval, one runner invocation made 14 actual exporter invocations. All 14 checks passed; zero failed checks, repairs, or retries.

- Supplied development example: exact Markdown bytes and expected parsed index, in an existing directory containing protected binary data.
- Changed two-record batch and changed destination: ID ordering, UTF-8 title, Unicode tag order, normalization, deduplication, empty tags, exact output file set.
- Empty batch: only `index.json` plus the preexisting protected file.
- Occupied card, occupied index directory, and dangling output symlink: exit 3, no output writes, complete fixture byte/link snapshot preserved, and a permission/alternate-destination request.
- Destination symlink: rejected before writing, preserving the snapshot.
- Later invalid record, duplicate ID, extra key, multiline title, nonstring tag, duplicate JSON key, and unpaired Unicode surrogate: rejected before writing, preserving the snapshot.

The 11 expected nonzero exits are successful negative checks, not discarded failures. Individual command vectors, exit statuses, stdout/stderr and assertions are retained in both the result JSON and actions log. Protected-file bytes matched in every case.

Manual packaging inspection confirmed matching folder/frontmatter name, an actionable relative helper path, and a description that includes local catalogue export while excluding existing-card editing and publishing. The helper's actual execution establishes basic syntax/import viability. No separate host format validator was available in the supplied materials; that check is unrun.

## Assumptions and limits

- Requires POSIX Python 3 with directory-relative file operations and `O_NOFOLLOW`. No non-POSIX test was run.
- Uses Python Unicode strip/lower and code-point sorting. Nonempty whitespace-only titles remain unchanged, as the brief says nonempty rather than nonblank.
- Single-line validation rejects Unicode line separators as well as CR/LF; duplicate JSON keys are rejected as malformed.
- Conservatively rejects every destination symlink component and `..` path component; the consumer must provide a direct authorized path. It does not support replacing occupied outputs even if separately approved.
- Assumes a stable destination during export. Exclusive file creation protects occupied targets, but multi-file atomic commit is unavailable. Process-kill, concurrent mutation, permission failure, disk-full behavior, and rollback are untested. The coordinator expressly did not authorize induced rollback/deletion tests, and none ran.
- Only synthetic local operation was observed. This is a focused usable prototype for the tested envelope, not evidence of comparative superiority, general host selection accuracy, or independent fresh-agent usability.

## Next step

For authorized use in the tested envelope, supply a valid UTF-8 input file and an existing direct-path destination whose exact card/index targets are absent, then follow SKILL.md. Obtain separate authorization and stronger evidence before considering overwrite support or concurrent exporters.

## Effort record

Coordinator deadline: 2026-10-02 21:17:56 UTC, ten minutes from admission (approximately 21:07:56). First observed clock reminder was 21:08:08. Test results were available at approximately 21:13:15. No monotonic timing instrumentation was used. As of this report write, there have been 10 top-level tool calls (including two coordinator messages), one approved test-runner launch, and 14 exporter process launches. Final inspection/count is appended below. All actual attempts and outputs are retained.

Finalization used 11 top-level tool calls: nine functions.exec calls and two coordinator messages. Of the nine nested actions, seven were exec_command and two were apply_patch. This includes the final inspection, with no new exporter or runner attempts. Approximate completion time: 2026-10-02 21:15 UTC, about seven and a half minutes from admission; not instrumented.
