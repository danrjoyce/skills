# R10 evidence and reproduction

Start with the [report and decision](report.md). R10 is terminal: twelve correct positive artifacts and six expected boundary refusals; all policies tied. Reporting interruptions and unknown action coverage prevent calling this an end-to-end 18/18 pass.

## Evidence map

- [Protocol](protocol.md), [fixed assignments](assignments.json), [original freeze](freeze.json): declared task, order, budget and scoring boundaries.
- [Consumer results](consumer-results.json), [event ledger](ledger.jsonl), [author-block snapshot](author-block.json): final consumer accounting and historical author accounting. The author-block snapshot's zero-consumer fields describe its 21:49 checkpoint, not final R10 status.
- [Carryover](carryover-reconciliation.json), [input preservation](input-preservation.json), records/: initial/final manifests, admissions, semantic reviews and exact second-use baselines.
- fixtures/: source inputs, expected batch bytes, protected starting state, and [draft claim checklist](fixtures/draft/claims.json). briefs/: supplied author examples.
- consumers/: actual final synthetic inputs, outputs and available attributed action/report files. Draft-template-first has no report file. Final manifests include omitted runtime prompt hashes.
- packages/: four selected generated packages, unchanged after selection. Author development source/results and failed attempts are in records/.
- public-prompts/: curated task/policy prompts; [curation manifest](prompt-curation.json) identifies the omitted private coordination paragraph and both hash sets. Originals are locally retained and not publicly reconstructable from these copies.
- [Checker addendum](checker-addendum.json): disclosed original newline-normalization flaw and separate byte-correct checker. Original checker/freeze bytes are unchanged.
- [Publication verification](../verification-r10.md) and [independent final review](final-review.md) and [its prompt](continuation.md).

## Read-only mechanical checks

From this directory, run existing Python:

    python3 check-artifacts-v2.py batch first consumers/batch-v2-first
    python3 check-artifacts-v2.py draft second consumers/draft-v2-second records/draft-v2-second-baseline.md

Use the corresponding family/use/workspace for each declared slot. Supply records/draft-{policy}-second-baseline.md for every draft second use. These commands compare retained final artifacts with declared expected/protected state; they do not execute generated helpers or reconstruct full action history. Inspect the six positive draft documents against the fixed claim checklist and sources for semantic correctness. Equivalent faithful prose is valid.

## Custody and scope

Only curated UTF-8 synthetic research evidence is published. Original private coordination prompts, runtime prompt.txt copies, coordination utilities/checkpoints, Python caches, binary/raw/compressed archives and all denied R6 payloads are excluded. The original freeze and workspace manifests retain hashes of omitted prompt bytes; private coordination material is not reproduced. Local author runtime contains additional development scratch outputs beyond the selected records. This publication preserves the outputs and evidence used for the report, but it is not a complete host transcript or a public clone of every runtime byte.

No new trials belong to reproduction of this report. Re-executing generated helpers would be a new operation with its own scope and review requirements. This assessment offers narrow synthetic artifact evidence, no observed v2 preference, and no general safety/cost/native-host conclusion.
