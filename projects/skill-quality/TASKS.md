# Task ledger

Updated: 2026-10-02. Only one substantive task may be active.

## Status vocabulary

Pending, active, completed, blocked. "Completed" means the stated artifact and checks exist; it does not imply empirical validation or endorsement.

## Sequential plan

1. **R1: Establish foundations and evidence triage. COMPLETED**
   - Inspect repository guidance and current public implementations.
   - Produce an initial rigorous answer to "How to determine if a skill is good?"
   - Include construct validity, causal marginal usefulness, activation, task distributions, generalization, reliability, safety, cost, maintainability, environment constraints, contamination, and an evaluation protocol.
   - Keep a source register with version pins, evidence quality, claim scope, and limitations.
   - Acceptance: substantive first draft and research records on a branch, remotely verified; exact fresh-context critique prompt recorded. No final meta-skill yet.
   - Completed checkpoint: substantive draft, source register, implementation audit, methodology, and source pins published. All eight original project files remotely verified byte-for-byte at `abbb267774acafdb8cfaad70b7b8dea3b1ae8f27`. Local text/link/JSON checks passed. See [verification record](research/verification-r1.md). This completes a research draft, not empirical validation.
2. **R2: Independently critique the foundations. COMPLETED**
   - Fresh context, no private reasoning from R1.
   - Verify important citations and definitions. Seek counterexamples and methodological weaknesses.
   - Deliver a prioritized critique with concrete revisions and unresolved questions.
   - Completed: [independent critique](research/critique-01.md), approximately 5,300 words, with nine prioritized findings, source/code checks, counterexamples, strengths, empirical gaps, and R3 acceptance criteria. All nine public implementation blob pins matched. Main analysis and R1 evidence artifacts left unchanged.
   - Key corrections: distinguish fitness from superiority; specify the callable/runtime contract; reconcile SkillsBench v4; preserve the fair Anthropic selection-set finding and add static probe-interference risks; formalize creator evaluation and proportionate measurement. No creator or benchmark was executed.
3. **R3: Revise and settle the measurement model. COMPLETED**
   - Respond to each critique item with evidence or a recorded uncertainty.
   - Freeze a defensible initial decision framework and identify remaining evidence needs.
   - Completed: [C1-C9 response ledger](research/revision-01.md), revised main framework, source dispositions/version reconciliation, expanded static implementation audit, integration-guide pin, methodology, and R4 prompt.
   - Separates fitness/adoption/superiority, defines the initial host-loaded workflow, nested creator-policy estimands and information boundaries, observable metrics, risk-proportionate costs, missingness/inference rules, and supply-chain threat model.
   - All ten public blob pins independently matched. Empirical questions are deferred explicitly, not marked solved. No creator or benchmark was executed. Publication checks: [R3 verification](research/verification-r3.md).
4. **R4: Design the comparative evaluation. COMPLETED**
   - [Protocol](research/comparative-protocol.md), [synthetic fixture specifications](research/evaluation-fixtures.md), [record schema](research/evaluation.schema.json), and [not-started pilot manifest](research/pilot-manifest.json) define the two-level comparison.
   - Proposes a USD 0 new-spend common-host exploratory pilot: three core briefs, four creator policies plus no-added-package control, 60 downstream episodes, 12 short routing policies, exact resource caps and all-attempt accounting.
   - Preserves native-baseline fidelity limits, shared-environment contamination, absent independent custody, incomplete telemetry and model nondeterminism. Stronger confirmation has explicit units, power assumptions, margins and resource gates.
   - Local schema/link/arithmetic checks are recorded in [R4 verification](research/verification-r4.md). No creator implementation, model trial, calibrated runtime grader, native compatibility result or superiority finding exists.
5. **R5: Implement a candidate skill-creation skill. COMPLETED**
   - Implement a standard research-only package at `projects/skill-quality/candidate/evidence-skill-creator/`, with repository-consistent invocation metadata, without installation or promotion.
   - Implement only justified authoring requirements and minimal synthetic fixture/recording support; run deterministic local checks only.
   - Completed: six-file [research candidate](candidate/evidence-skill-creator/SKILL.md), [design/traceability](research/r5/design.md), [local fixture/oracle/adapter/record support](research/r5/README.md), original/revised candidate and support freezes, protocol clarifications and reproducible calibration evidence.
   - Verification: 33 tests; twelve oracle controls twice, eleven instrument replays and six fixed routing annotations; two identical 394-file evidence bundles; public pinned validator, syntax/metadata/hash/link checks. See [R5 verification](research/verification-r5.md).
   - One generic inspector defect repaired with disclosed freeze revision; all five other candidate files unchanged. Zero model trials. Native activation, live grader qualification, full source closures and execution supervision remain R6 preflight gates.
6. **R6: Run comparative tests and adversarial validation. BOUNDED DIAGNOSTIC COMPLETE; PRIMARY BLOCKED**
   - Qualify the actual common-host environment and full pinned baseline closures before launch. Use fresh reset state, while disclosing shared-environment exposure; do not pretend isolation is enforced.
   - Follow the USD 0 ceiling and all caps in the exact [R6 handoff](HANDOFF.md); primary discovery must not be silently replaced by explicit loading. A blocked-preflight report is an honest outcome.
   - Archive outcomes, costs, artifacts, failures, and confidence limits.
   - R6 final: 17 fresh worker admissions, four frozen D1 packages, one A0 development solver, ten fixed downstream cells, loading qualification and four-artifact semantic qualification. N0 artifact correctness 2/2; C0/T0/O0/A0 each 0/2 on an existing-output-directory incompatibility. No retries, repairs or fallback. A0 documentation cutoff and semantic timing uncertainty retained. Original 84 primary cells remain methodology-gated/unrun. See the [final report](research/r6/report.md), [verification](research/verification-r6.md), and [exact R7 critique prompt](research/r6/continuation.md).
7. **R7: Independently critique the bounded result. COMPLETED**
   - [Critique C1-C10](research/r7/critique.md) independently checks the published and accessible local evidence, addresses contract fairness and legitimate stopping, baseline fidelity, selection, units, provenance, timing and practical usefulness.
   - All 26 public source blobs matched fresh complete pinned trees. Selected packages and freezes remain unchanged; ten existing mechanical reports replayed without new trials.
   - [Terminal-status correction](research/r7/r6-status-addendum.md) records the conservative setup-bound overshoot and loading/semantic timing uncertainty. No verified active-time, full-action or superiority claim.
   - Next: a concrete smaller v2, not more generic evaluation machinery. Verification is recorded [here](research/verification-r7.md).
8. **R8: Implement a proportionate v2 creator. COMPLETED (STATIC IMPLEMENTATION)**
   - [Two-file v2](candidate/evidence-skill-creator-v2/SKILL.md), 664 words and 4,665 bytes, has a short authoring path and explicit material starting-state/authority contract. Collision refusal and uncertain-outcome reconciliation remain.
   - [C1-C10 response and compatibility](research/r8/README.md), [new freeze](research/r8/candidate-freeze.json), [static checks](research/r8/static-results.json), and [verification](research/verification-r8.md). V1 and all historical nontracking evidence are preserved.
   - Zero new model/helper/semantic trials. [Later assessment](research/r8/assessment-plan.md) is proposed only; there is no R6 restart or budget refund. The first-use requirement is implemented in instructions, not demonstrated by R8.
9. **R9: Independently review v2 readiness. COMPLETED (STATIC REVIEW)**
   - [Independent review](research/r9/review.md) accepts the frozen package as ready for a separately authorized limited assessment. No material package defect or further rewrite is required by inspection.
   - Inputs/state/outputs/tools/authority, file and non-file counterexamples, trigger metadata, evidence boundaries and small-update proportionality checked. Deterministic package/freeze and historical preservation checks passed; no live trial or native loading test. [Verification](research/verification-r9.md).
   - The proposed assessment is proportionate after three launch clarifications: second-use state carryover/direct-control fairness, the intervention outcome, and feasible per-slot stopping/evidence retention. Maximum trial durations plus preparation leave seven minutes of interim overhead before the experimental stop; all 22 slots are a ceiling, not guaranteed completion.
10. **R10: Assess bounded usefulness. COMPLETED**
   - [Frozen protocol](research/r10/protocol.md) settled state carryover, direct-control reuse, intervention definitions and termination headroom before observations. The fixed four authors and eighteen consumers were each admitted once; no replacement, resume, extra case or candidate tuning.
   - [Observed result](research/r10/report.md): each policy has 4/4 correct positive artifacts and 2/2 correct boundaries, with zero task interventions supplied. All eighteen protected-state checks passed. No observed v2 preference under the predeclared rule.
   - Four consumer reporting interruptions, fourteen completed final notifications, seventeen report files and nine completed notifications observed within the cap remain distinct. Two author reporting interruptions, one failed development oracle followed by autonomous harness repair, and one pre-execution source-review/capture race are preserved.
   - [Curated evidence/reproduction](research/r10/README.md) and [verification](research/verification-r10.md). Original candidate packages, all fifty R10 frozen inputs and prior nontracking evidence remain unchanged. No installation, promotion, merge, paid API call or native-loading result.
11. **Final independent review. COMPLETED**
   - [Independent final review](research/r10/final-review.md) checks retained source/output bytes, arithmetic, draft semantics, carryover, timing, missingness and the frozen v2 package. The [review prompt](research/r10/continuation.md) records its scope.
   - No artifact-score defect changes the no-preference conclusion. A minor fifteen-versus-sixteen attributed author-call discrepancy is recorded explicitly without altering original evidence. Publication identity/CI checks are separate and recorded in [verification](research/verification-r10.md).
   - Research, creation and review stop with this deliverable. The package and rigorous analysis are available for user review; broader instrumented/native-host validation is unexecuted optional future work requiring a concrete purpose and authorization. There is no active further trial or report-only campaign.

## Checkpoints

- 2026-10-02: Repository inspected at `3cca18b368ae95cdbdebbff572ccafa662551015`. No existing project or research branch found. Created `research/skill-quality`. Root `AGENTS.md` resolves to `CLAUDE.md`; project research will remain outside shipped skill buckets. Repository prose prohibits em dashes.
- 2026-10-02: Scaffold published at `dcf2ec650120d4a2cd86cbcef4f1fe61d81783c2`; [draft PR #1](https://github.com/danrjoyce/skills/pull/1) opened. The first substantive draft is approximately 5,400 words. Public implementations are pinned and the main proposed framework is separated from measured results.
- 2026-10-02: R1 substantive commit `abbb267774acafdb8cfaad70b7b8dea3b1ae8f27` verified remotely. Comparison with the original main shows only project-document additions; no existing skill or configuration changed. No PR-triggered workflow run or commit status was returned for that commit. Stop here and renew context for R2; the exact critique prompt is in HANDOFF.md.

- 2026-10-02: R2 independently reviewed remote project commit `9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8`. Published critique and updated project tracking only. The revised evidence review must address the June 2026 SkillsBench v4; the linked SWE-Skills-Bench repository returned 404 during verification. These findings do not constitute benchmark replication. R3 is the next substantive task.

- 2026-10-02: R3 revised from `ca27f690562c7440458dc50cdc0f01b5073f08ad`, preserving R2 critique and R1 verification unchanged. Conceptual acceptance criteria addressed; runtime/benefit/custody and actual resource/value decisions remain open. R4 is next in fresh context; no R5 implementation or paid experiment is authorized by this checkpoint.

- 2026-10-02: R3 substantive revision `90b16afb072f1d2ecfd7297664b7281c33e33e9e` verified byte-for-byte across all 12 project files. GitHub comparison showed exactly ten intended project-document/pin changes and no unrelated paths. No workflow/status/check run was reported for this commit; local research validation passed. The tracking-only checkpoint records these checks.

- 2026-10-02: R4 designed from `ff852c9e979302c937aceb82f8dca557294c8e73`. Provisional engineering choices resolve routine scope decisions so R5 can proceed; paid/native confirmation, independent custody and owner-validated adoption margins remain gated. The first pilot is expressly public and exploratory, not an independent holdout. No experiment was run.

- 2026-10-02: R4 substantive design `55ab7f0f2941ba0f0801c889962f9bbf1af91fc6` verified remotely across all 18 project files. Exactly nine project paths changed; no workflow/status/check run was returned. Static schema, 99 local links/anchors, budgets and conditional power arithmetic passed. Final documentation checkpoint adds the verification record and explicit public-evidence sanitization guidance. R5 implementation is the next context-bounded task.

- 2026-10-02: R5 implemented from `ed3e468139f6f90eb8c954989ea95a123c161801`. Candidate workflow froze before fixture details; fresh-context review strengthened evidence custody, Git semantic-state checks, malformed-input handling and failure/fallback/cap accounting. Original fifteen nontracking research files remain byte-identical. Candidate tree: `4dc5eef71128fcb98b2ab27c6163a91fc701c91854a8ba3df9dafa9965b55683`. R6 is next in fresh context; no runtime comparison or native compatibility claim. Publication checks: [R5 verification](research/verification-r5.md).

- 2026-10-02: R5 substantive commit `94b572a5592076284a99ae5a4640f7ed109d8aef` independently verified byte-for-byte across all 45 project files. Full-tree/commit comparison found exactly 30 intended project changes; original-main comparison contains only project additions. No workflow run, status or check run returned. Final tracking-only checkpoint records these checks, with no candidate/support change.

- 2026-10-02: R6 paused for conservative context renewal with all three started workers terminal. Candidate/support and original R1-R4 evidence remain unchanged. Selected C0/T0 artifacts and all known attempts are retained in the runtime archive. O0/A0, ten downstream cells, live semantic qualification and final report remain pending; R7 has not started.

- 2026-10-02: R6 bounded diagnostic completed without candidate tuning. All ten downstream attempts retained. Complete action and exact cost telemetry remain unknown; no superiority or native-performance finding. R7 begins only in fresh context after verified publication.

- 2026-10-02: R6 substantive commit `7833edd1edb6dc038fa30cbb90bf1ec4ac5f5ad2` verified across all 102 published project files, with exactly 60 intended changed paths and no outside changes. Exact-commit workflow/status/check-run queries returned zero, not a CI pass. Three compressed archives remain local after the disclosed authorization denial; curated synthetic replay evidence and pinned source URLs/hashes are published.

- 2026-10-02: R7 began from confirmed remote `0e66e7eff6899f9e3082cbe9d67c3e9847966b1e`. PR metadata was stale and the local terminal stop record postdated the published journal. Independent review supplies a status addendum without rewriting R6 evidence. The next substantive task is a usable, smaller v2 in R8, with no new trials in that implementation context.

- 2026-10-02: R8 began from confirmed remote `fbc7a59232c1d74c4928b385cd8b7e1a5d08613c`. V2 frozen at `cd74d8380c5aefbdc3ae4b8b77e2fd59a74323c5ecbb714a17a20e972afe53a9`; local static format and preserved-v1/support checks passed. No live trial, installation, archive upload, campaign reset or settings change. Publication evidence is recorded in [R8 verification](research/verification-r8.md).

- 2026-10-02: R9 reviewed remote `08c73746c256fbed73910b13f09589b510e96231` in a fresh context and accepted package readiness for a separately authorized limited assessment. V1, v2 and R1-R8 evidence remain frozen. No new experiment, native activation or raw archive access/upload. The review ends with the scope and authorization gate recorded in [R9 verification](research/verification-r9.md).

- 2026-10-02: R10 used one new 20:58-23:58 UTC budget, with a 23:28 experimental stop. All 22 admissions were terminal by 22:50:28. The artifact/boundary comparison tied; reporting/timing limits were retained. Curated publication excludes original coordination prompts, runtime prompt copies, caches and denied R6 archives. [Verification](research/verification-r10.md) records exact remote publication rather than assuming it.

- 2026-10-02: R10 substantive publication `3e2791c5cfcd68f3311e96a26182a82174ce293d` was independently fetched across all 300 intended changed files. Full tree comparison found three tracking replacements and 297 additions, preserving all 280 other existing blobs/modes. Exact-commit workflows/statuses/checks returned zero; CI is absent. Final independent review found no material score or recommendation defect. Research, creation and review are complete, with no active further campaign.
