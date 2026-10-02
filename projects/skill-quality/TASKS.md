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
5. **R5: Implement a candidate skill-creation skill. PENDING**
   - Implement a standard research-only package at `projects/skill-quality/candidate/evidence-skill-creator/`, with repository-consistent invocation metadata, without installation or promotion.
   - Implement only justified authoring requirements and minimal synthetic fixture/recording support; run deterministic local checks only.
   - Freeze candidate, adapter and development support with exact version/evidence labels for R6; do not execute a model comparison during R5.
6. **R6: Run comparative tests and adversarial validation. PENDING**
   - Use isolated environments and frozen baselines.
   - Archive outcomes, costs, artifacts, failures, and confidence limits.
7. **R7: Critique, refine, and report the bounded result. PENDING**
   - Fresh-context review and held-out confirmation.
   - State where the candidate improves, ties, loses, or remains unproven.
   - Promote only after evidence and explicit merge authorization.

## Checkpoints

- 2026-10-02: Repository inspected at `3cca18b368ae95cdbdebbff572ccafa662551015`. No existing project or research branch found. Created `research/skill-quality`. Root `AGENTS.md` resolves to `CLAUDE.md`; project research will remain outside shipped skill buckets. Repository prose prohibits em dashes.
- 2026-10-02: Scaffold published at `dcf2ec650120d4a2cd86cbcef4f1fe61d81783c2`; [draft PR #1](https://github.com/danrjoyce/skills/pull/1) opened. The first substantive draft is approximately 5,400 words. Public implementations are pinned and the main proposed framework is separated from measured results.
- 2026-10-02: R1 substantive commit `abbb267774acafdb8cfaad70b7b8dea3b1ae8f27` verified remotely. Comparison with the original main shows only project-document additions; no existing skill or configuration changed. No PR-triggered workflow run or commit status was returned for that commit. Stop here and renew context for R2; the exact critique prompt is in HANDOFF.md.

- 2026-10-02: R2 independently reviewed remote project commit `9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8`. Published critique and updated project tracking only. The revised evidence review must address the June 2026 SkillsBench v4; the linked SWE-Skills-Bench repository returned 404 during verification. These findings do not constitute benchmark replication. R3 is the next substantive task.

- 2026-10-02: R3 revised from `ca27f690562c7440458dc50cdc0f01b5073f08ad`, preserving R2 critique and R1 verification unchanged. Conceptual acceptance criteria addressed; runtime/benefit/custody and actual resource/value decisions remain open. R4 is next in fresh context; no R5 implementation or paid experiment is authorized by this checkpoint.

- 2026-10-02: R3 substantive revision `90b16afb072f1d2ecfd7297664b7281c33e33e9e` verified byte-for-byte across all 12 project files. GitHub comparison showed exactly ten intended project-document/pin changes and no unrelated paths. No workflow/status/check run was reported for this commit; local research validation passed. The tracking-only checkpoint records these checks.

- 2026-10-02: R4 designed from `ff852c9e979302c937aceb82f8dca557294c8e73`. Provisional engineering choices resolve routine scope decisions so R5 can proceed; paid/native confirmation, independent custody and owner-validated adoption margins remain gated. The first pilot is expressly public and exploratory, not an independent holdout. No experiment was run.
