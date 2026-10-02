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
2. **R2: Independently critique the foundations. PENDING**
   - Fresh context, no private reasoning from R1.
   - Verify important citations and definitions. Seek counterexamples and methodological weaknesses.
   - Deliver a prioritized critique with concrete revisions and unresolved questions.
3. **R3: Revise and settle the measurement model. PENDING**
   - Respond to each critique item with evidence or a recorded uncertainty.
   - Freeze a defensible initial decision framework and identify remaining evidence needs.
4. **R4: Design the comparative evaluation. PENDING**
   - Declare creation-task and downstream-task distributions, baselines, budgets, holdout ownership, grading calibration, safety gates, uncertainty analysis, and stopping rules before implementation.
   - Distinguish testing a creator from testing a skill it creates.
5. **R5: Implement a candidate skill-creation skill. PENDING**
   - Follow repository packaging and invocation rules.
   - Implement only requirements justified by the research and protocol.
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
