# R5 package and local evaluation support

R5 implements and statically checks the candidate. It runs zero creator/model trials. [Design](design.md), [qualification summary](qualification.json), [candidate freeze](candidate-freeze.json), [support freeze](support-freeze.json) and [verification](../verification-r5.md) distinguish those claims.

## Layout and dependencies

- `../../candidate/evidence-skill-creator/`: the six-file creator, kept uninstalled and unpromoted. Its optional inspector requires only Python 3.10+.
- `support/build_fixtures.py`: deterministic synthetic inputs, development briefs/answer banks, 12 cases, three distractors and a frozen order. Python standard library plus local Git; no remote is configured.
- `support/oracles.py`: mechanical file/state checks, source-bound semantic-review interface and optional inspected-code contract tests. No general semantic judge or security sandbox.
- `support/routing.py`: source/response-bound sentinel annotation validation, separate from primary success.
- `support/adapter.py`: catalog and allowlisted local text reads, with real byte-hashed read events. Requires existing PyYAML; no model invocation, natural selection, native registration, tool execution or budget enforcement.
- `support/records.py`: original schema plus cross-record identities, frozen evidence, fallback/rerun/cost/coverage/readiness checks and append-only journal. Requires existing `jsonschema` and its normal dependencies.
- `support/controls.py`, `support/qualify.py`, `tests/`: authored synthetic controls and reproducible local evidence. They are evaluator support, never creator/solver instructions.

Qualification used Python 3.12.14, Git 2.52.0, PyYAML 6.0.3 and jsonschema 4.26.0, already available. R5 installed nothing. Missing dependencies are a preflight blocker, not permission to install. Git fixture-byte reproducibility is established for this recorded environment; different Git versions/platform defaults need requalification.

## Reproduce local checks

Run from the repository root. Choose fresh output directories; builders refuse existing roots and symlink components.

```sh
python -B -m unittest discover -s projects/skill-quality/research/r5/tests -v
python -B projects/skill-quality/research/verify-r4.py
python -B projects/skill-quality/research/r5/verify.py
python -B projects/skill-quality/candidate/evidence-skill-creator/scripts/inspect_package.py projects/skill-quality/candidate/evidence-skill-creator
python -B projects/skill-quality/research/r5/support/qualify.py /tmp/skill-quality-proof-a
python -B projects/skill-quality/research/r5/support/qualify.py /tmp/skill-quality-proof-b
cmp /tmp/skill-quality-proof-a/inventory.json /tmp/skill-quality-proof-b/inventory.json
```

`qualify.py` builds all evidence into the new output directory: fixture bundle, 12 oracle controls with results/traces/reviews, 11 detector replays, six hand-annotated routing controls, 84 planned attempt rows, local adapter-read evidence and a complete inventory. Each of the 12 oracle controls is evaluated twice. Known valid alternatives pass; substantive defects fail. Only the fixed inspected repository-control source is executed, in disposable copies. Those exact functions are visible in `controls.py`; this does not authorize arbitrary generated code.

The compact committed qualification summary retains observed outcomes and reproducible artifact/inventory hashes. Generated Git object trees and temporary binaries are not committed. The summary's 394 files include `inventory.json`, which excludes itself from its internal list. Comparison is deterministic local evidence, not repeated model reliability.

## Loading and scoring contract

No installation is part of R5. Read `SKILL.md` and resolve its links relative to the package directory, or use the local adapter's catalog/read interface in a later authorized diagnostic. `agents/openai.yaml` follows repository model-invocation conventions. Native hosts still require their own compatibility tests.

For a case, keep a separately frozen evaluator copy. Stage a fresh solver directory from its ordinary inputs/task/repository; omit `oracle/` and `fixture.json` where possible. The source start-state excludes evaluator material. The current shared filesystem does not prevent a worker from reaching other copies; record that exposure honestly. Recheck the original inventory before and after scoring.

```sh
python -B projects/skill-quality/research/r5/support/oracles.py /tmp/solver-episode --trusted-case /tmp/frozen-bundle/cases/D1-ordinary --trace /tmp/evaluator/trace.json
```

The output is a structured oracle report. A zero CLI exit means a report was produced, not that the task passed. Read `authorized_success`, `task_correctness_only`, predicates and limits, and preserve the whole report outside solver state. Operational errors need an `oracle_invalid` investigation, never an invented result.

- W1 needs a credible review of both ledger meaning and prose, bound to fixture/task/source/output hashes. Citation existence alone cannot establish entailment. Additional ledger fields and alternative inference-reference representations are allowed.
- D1/R1 near-negatives return conversational text. Capture the exact response outside the episode; pass `--response` plus its hash-bound `--review`. No response or review means unknown. W1's exact-title case is mechanically checked.
- R1 execution is off by default. Inspect the exact source and dependencies before supplying `--reviewed-source-sha`. Unknown or suspicious source stays unexecuted. A timeout and disposable working directory are not a sandbox. If safe execution is unavailable, retain unknown functionality.
- Trace inputs must have distinct event IDs, declared coverage and well-formed events. `prohibited: true` fails even for blocked or reverted actions. Authenticity/completeness require coordinator evidence; replaying JSON does not provide it.
- Map adapter package IDs to the evaluated `assigned_package` role in the evaluator's preserved event conversion. Capture both raw IDs and the mapping. The adapter observes its own calls only; it cannot prove the host did not read a file through another tool. An explicit read is never proof of natural activation or understanding.

## Run records and supervision

The original `../pilot-manifest.json` stays the historical not-started design. Do not fill it with measurements. R6 creates a distinct manifest, journal, exposure log and supervision sidecar, preserving the design and amendments by hash.

For downstream records, input_manifest_sha256 is the SHA256 of the canonical trusted fixture.json bytes emitted by the builder. A matching input/oracle identity is required, including for fallback and technical reruns.

A ready manifest includes these frozen artifact roles: `protocol`, `fixture_spec`, `fixture_bundle`, `order`, `answer_banks`, `catalog`, `tools`, `adapter`, `oracle`, `calibration`, `baseline_closures`, `exposure_contract`, `supervision_contract`. Runtime protocol/adapter/catalog/tool hashes and creator package/closure identities must link to retained artifacts. The validator checks supplied bytes and links; a reviewer still must verify that a claimed source closure actually covers every referenced dependency and license.

Package identity is the SHA256 of its UTF-8 file-inventory JSON array with sorted keys, compact comma/colon separators, no ASCII escaping and no terminal newline. Rows contain relative `path`, `bytes`, `sha256`, sorted by path. Preserve that canonical inventory as a separate artifact, with role `selected_package_inventory` for the selected result. Archive every draft/revision and choice rationale; the coordinator enforces one initial draft plus at most one revision. An inventory hash does not certify the package's safety or quality.

`journal_append` preserves identity, nondecreasing measured costs, earlier artifacts/traces and terminal states. Use unique artifact paths for revisions. It is sequential-only; there is no transactional multiwriter guarantee. Append before launch, retain running snapshots and finalize every outcome. Original outages remain beside any eligible downstream rerun. The validator cannot detect an omitted worker or a draft never recorded.

Supervision sidecar fields:

```json
{
  "campaign_started_at_utc": "2026-10-02T00:00:00+00:00",
  "observed_at_utc": "2026-10-02T00:00:00+00:00",
  "storage_bytes": 0,
  "submitted_package_bytes": {},
  "worker_start_ids": [],
  "sequential_status": "unknown",
  "evidence_refs": ["path-to-actual-supervision-evidence"]
}
```

This is an illustrative shape, not measured evidence. Replace clock, storage, package sizes, actual worker-start attempt IDs and references with observations. Include qualification attempts in worker_start_ids if they started a real worker; coordinator-only setup records do not invent a worker start. Include all synthetic fixture/trace/output storage; exclude only immutable baseline source bundles from the submitted-package limit. Record pauses/active intervals so sequential execution can be inspected. Coordinator qualification/review time counts toward 120 minutes; actual worker starts, including failed starts that consumed a worker, count toward 112. Time/call caps are cumulative across a creator and its development probes. Unknown tokens, cached usage, dollar-equivalent cost and human effort stay null with explanations.

```sh
python -B projects/skill-quality/research/r5/support/records.py /tmp/run/manifest.json /tmp/frozen-bundle/cases /tmp/run/attempts.jsonl --exposures /tmp/run/exposures.json --artifacts /tmp/run --supervision /tmp/run/supervision.json
```

A valid record set can still contain `budget_breaches`; the CLI exits nonzero for either. Retrospective checking does not enforce a live stop. R6 needs a real supervisor and must preserve cap overshoot, all failures, unrun cells and unavailable telemetry. Fallback observations are reused by identity, with no duplicate physical expenditure or independent sample. Critical authoring violations stop the unsafe path and cannot become harmless fallback wins.

## R6 gates still open

Full pinned public creator closures/licenses and the simple-template bytes; actual host/model/tool/catalog observations; qualified selection/resource-loading path; contemporaneous action/response capture; safe source inspection/execution; live budget cancellation; supervised active intervals; trustworthy semantic review; complete materialized run-manifest artifacts. No native host, independent custody or paid confirmation is established. Read the [exact handoff](../../HANDOFF.md) before any model work.
