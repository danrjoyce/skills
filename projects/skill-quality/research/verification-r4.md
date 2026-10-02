# R4 verification record

Date: **2026-10-02 UTC**. Scope: pre-implementation comparative protocol, synthetic task specifications, record schemas, planning arithmetic and publication. No model or creator experiment was run.

## Starting state and preserved work

- PR #1 was open and draft on `research/skill-quality`, head `ff852c9e979302c937aceb82f8dca557294c8e73`.
- All 12 starting project files were independently fetched at that exact commit and matched local UTF-8 bytes. Repository `AGENTS.md`, `CLAUDE.md` and `.agents/invocation.md` were read remotely.
- Revised main analysis, independent critique, response ledger, source register, public implementation audit/pins, methodology and historical verification records are preserved unchanged.
- R4 uses the prior immutable public pins. The public Anthropic creator's full text was reread at its pin; its file blob matched the existing manifest. The protocol explicitly requires complete baseline resource/dependency materialization later rather than claiming the selected-file audit is an executable package snapshot.

## Delivered design

- [Comparative protocol](comparative-protocol.md): approximately 6,800 words; two-level estimands, five comparison policies, explicit adaptations, failures/fallback, budgets, information limitations, qualification, threats, costs, missingness, decision regions and stopping
- [Fixture specifications](evaluation-fixtures.md): approximately 3,100 words; three synthetic workflow briefs, 12 downstream cases, three routing sentinels, 12 oracle controls and six instrument fixtures
- [Pilot manifest](pilot-manifest.json): valid not-started design, with runtime, package and grader identities unresolved rather than fabricated
- [JSON Schema](evaluation.schema.json): manifest, fixture and all-attempt record contracts; structural checks do not establish semantic correctness or enforcement
- [Static checker](verify-r4.py): local document/link, JSON/schema, rejected-bad-record and planning-arithmetic validation; no model calls
- Updated project README, TASKS and exact fresh-context R5 handoff

## Local verification

Run `python projects/skill-quality/research/verify-r4.py` from the repository workspace. It uses the already-installed `jsonschema` package; no dependency installation occurred. The checker validates:

1. Draft 2020-12 schema syntax and the design manifest
2. Rejection of a ready manifest with unresolved identities, new spend, a false holdout claim, a false unrun success record, negative tool counts, a nonsynthetic fixture and success with a failed required predicate
3. Unique method/brief/case identities, family/primary weight sums, attack-pair linkage and denominators
4. 12 full creation policies, 12 short routing policies, 60 downstream episodes, 112 maximum worker starts, 1,760 tool calls, 496 execution minutes and 616 total active campaign minutes
5. Conditional confirmation arithmetic: 480 creation policies, 4,320 downstream episodes, 408 ceiling execution hours; brief-cluster sizing sensitivities 60/153/951 under the stated SD assumptions
6. Break-even illustrations and the illustrative six-trial zero-failure bound
7. Local Markdown file/anchor destinations, JSON parsing and repository prose rules

Schema-control records are constructed only inside the checker and labeled synthetic/planned. They are not experimental attempts. No actual fixture builder, task oracle, model grader or candidate exists at R4. The checks demonstrate internal consistency of the proposed instrument contracts, not that they measure skill quality correctly.

The local checker passed, including 99 relative file/anchor destinations, all three schema record variants through synthetic controls, and the stated arithmetic. Python syntax parsing also passed. The changed-file allowlist is checked before publication. The intended scope is six new R4 research artifacts plus README, TASKS and HANDOFF, all under `projects/skill-quality/`. No shipped skill, plugin manifest, router, repository setting or upstream source is changed.

## Publication checkpoint

Pending substantive commit and independent remote byte/scope verification. A tracking-only update will record the verified substantive checkpoint here; the PR description will carry the final branch checkpoint without requiring this file to embed its own Git hash.

## Limits and next stage

- Design decisions and numerical margins are explicit engineering proposals, not observed results or user-approved universal acceptance values.
- The first pilot is public/exploratory with an unenforced shared-environment boundary. No independent holdout, absent pretraining contamination, exact model snapshot or deterministic harness is claimed.
- Native Codex/Claude Code hosts, native public-creator fidelity and complete runtime telemetry remain unverified. Common-host adaptation loses capabilities, including native loops and human feedback.
- USD 0 additional spending does not imply free computation; existing worker usage/time is counted and telemetry gaps stay unknown.
- The conditional powered design needs verified sizing assumptions, independent custody, qualified review and approved resources. It is not authorized or scheduled by R4.
- R5 may implement and statically test the research candidate and deterministic support. Comparative model execution belongs to the separate R6 stage after preflight.
