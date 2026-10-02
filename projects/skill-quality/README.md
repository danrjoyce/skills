# Skill quality research

Status: R8 has produced a smaller two-file v2 and deterministic static checks. Behavioral usefulness remains untested. Next: independent readiness review in a fresh context, then separately authorize any live assessment. R6 is closed; its original primary campaign remains gated/unrun, with no creator-superiority finding. Started 2026-10-02.

## Purpose

Determine what makes an AI-usable skill good, then develop and test a general skill-creation skill. The final aim is demonstrable improvement over strong public alternatives on declared task distributions, not an untestable claim of universal superiority.

This is a research project, not an installed skill. It does not change existing skills, plugin manifests, repository configuration, or upstream synchronization.

## Research contract

- Work on one substantive task at a time.
- Distinguish verified source claims, reasoned synthesis, proposed decision rules, and measured results.
- Prefer primary sources; evaluate empirical evidence separately from implementation authority.
- Pin implementations and preserve source anchors and uncertainty.
- Require fresh-context criticism and revision before implementing the final meta-skill.
- Keep evaluation data and holdouts separate from creation and tuning.
- Renew context conservatively around 50,000 to 60,000 tokens and always before the requested approximately 90,000-token ceiling. Checkpoint earlier at a coherent stopping point.
- Publish incremental work on a research branch and draft pull request. Do not merge.

## Navigation

- [Practical v2 creator](candidate/evidence-skill-creator-v2/SKILL.md): 664-word, two-file research candidate; [changes, calling/installation limits and C1-C10 responses](research/r8/README.md), [freeze](research/r8/candidate-freeze.json), [static results](research/r8/static-results.json), [verification](research/verification-r8.md), [proposed later assessment](research/r8/assessment-plan.md), and [exact next independent-review prompt](research/r8/continuation.md)

- [R7 independent critique](research/r7/critique.md), [terminal-status correction](research/r7/r6-status-addendum.md), [review checks](research/r7/evidence-review.json), [verification](research/verification-r7.md), and [exact R8 implementation prompt](research/r7/continuation.md)

- [R6 final bounded report](research/r6/report.md), [predeclared diagnostic](research/r6/diagnostic-protocol.md), [attempt journal](research/r6/journal.jsonl), [retained source-archive manifest](research/r6/retained-evidence-manifest.json), [retained runtime-archive manifest](research/r6/retained-evidence-manifest.json), and [historical R7 critique prompt](research/r6/continuation.md)

- [Frozen v1 candidate](candidate/evidence-skill-creator/SKILL.md): six-file model-invocable creator, preserved unchanged and uninstalled
- [R5 guide](research/r5/README.md), [design/traceability](research/r5/design.md), [qualification summary](research/r5/qualification.json) and [verification](research/verification-r5.md): local support, 33 tests, twelve oracle controls twice, and explicit runtime limits

- [How to determine if a skill is good](how-to-determine-if-a-skill-is-good.md): the revised measurement and decision framework
- [Independent critique](research/critique-01.md): nine prioritized findings, verified code/source checks, and revision acceptance criteria
- [R3 response ledger](research/revision-01.md): C1-C9 dispositions, independently checked evidence, and remaining decisions
- [Comparative evaluation protocol](research/comparative-protocol.md): bounded no-extra-spend pilot, explicit comparison policies, information limits, and separately gated confirmation plan
- [Fixture/task specifications](research/evaluation-fixtures.md): synthetic task contracts, answer banks, and oracle controls for R5
- [Pilot design manifest](research/pilot-manifest.json) and [record schema](research/evaluation.schema.json): not-started machine-readable design, fixture and attempt contracts
- [R4 static checker](research/verify-r4.py) and [verification record](research/verification-r4.md): reproducible document/schema/arithmetic checks, not a model experiment
- [R3 verification record](research/verification-r3.md): checks and publication limits
- [Source register](research/source-register.md): evidence quality, claim scope, and limitations
- [Implementation audit](research/implementation-audit.md): exact public-code observations and methodological critique
- [Implementation pins](research/implementation-pins.json): machine-readable commit and blob identifiers
- [Methodology](research/methodology.md): search approach, verification, and unresolved questions
- [R1 verification record](research/verification-r1.md): publication checks and their limits
- [TASKS.md](TASKS.md): sequential task ledger and acceptance criteria
- [HANDOFF.md](HANDOFF.md): current state and exact restart prompt

Both creator versions remain uninstalled research artifacts. V2 is implemented and statically checked; its effectiveness, native compatibility and advantage over a direct solver or simple template remain unproven. The published R6 cases are known development evidence for v2, with no independent holdout custody. Static checks and a shorter package do not prove better decisions.
