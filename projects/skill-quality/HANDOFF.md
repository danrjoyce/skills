# Research handoff

Updated: **2026-10-02 UTC**.

## Current state

**R1-R4 are complete through comparative-protocol design. R5 research-candidate implementation is next.** Continue on `research/skill-quality` and [draft PR #1](https://github.com/danrjoyce/skills/pull/1), based on main at `3cca18b368ae95cdbdebbff572ccafa662551015`. Inspect the actual branch tip before writing; do not recreate the branch or PR.

R3's substantive revision is `90b16afb072f1d2ecfd7297664b7281c33e33e9e`; its verified tracking checkpoint `ff852c9e979302c937aceb82f8dca557294c8e73` is R4's starting point. R4 preserves the revised main analysis, independent R2 critique, R3 response ledger, public pins and historical verification records. The PR and [R4 verification](research/verification-r4.md) identify the new publication checkpoint.

No candidate, model-performance experiment, runtime compatibility result, calibrated downstream grader, independent holdout, or superiority finding exists. R4 supplies concrete engineering proposals so implementation can proceed. It does not pretend that model determinism, enforceable isolation, native runtimes or paid resources have been established.

## Read these artifacts

1. [Comparative protocol](research/comparative-protocol.md), especially sections 1-6, 8-10
2. [Fixture/task specifications](research/evaluation-fixtures.md), exact contracts, calibration controls and answer banks
3. [Pilot design manifest](research/pilot-manifest.json) and [record schema](research/evaluation.schema.json), explicitly not-started
4. [Revised main analysis](how-to-determine-if-a-skill-is-good.md), sections 1.4, 2.3, 3, 6.4, 7, 9 and 11
5. [R3 response ledger](research/revision-01.md) and [independent R2 critique](research/critique-01.md)
6. [Implementation audit](research/implementation-audit.md), [source pins](research/implementation-pins.json) and [source register](research/source-register.md)
7. [TASKS](TASKS.md), [R4 verification](research/verification-r4.md) and [static checker](research/verify-r4.py)

## Decisions to preserve

- Fitness, incremental value, adoption and superiority are distinct. No universal scalar quality score, fabricated winner or significance-to-equivalence shortcut.
- First product is a standard host-loaded, model-invocable authoring workflow. It is not a registered native function/MCP service. Native Codex/Claude Code are intended targets, untested.
- Research candidate location: `projects/skill-quality/candidate/evidence-skill-creator/`. Keep it uninstalled and outside promoted skill/plugin/router lists. Include standard `SKILL.md` and repository-consistent `agents/openai.yaml`; R7 can decide promotion separately.
- Three provisional synthetic families: inventory CSV normalization, closed-source evidence briefs and miniature Python repository maintenance. No sensitive user data or live external effects.
- Pilot conditions: direct solver with no added task-specific package, simple-template creator, pinned OpenAI and Anthropic creators with declared common-host adaptations, and candidate. The same visible background tools/skills may remain; do not call it a pristine no-skill model.
- Core pilot: 12 full creation policies, 12 short routing policies, 60 downstream episodes, at most four technical downstream reruns. USD 0 new external spending, 112 worker starts, 1,760 tool calls, 616 active campaign minutes, sequential work. These are upper bounds, not required consumption. Primary success uses six eligible cases; attacks/near-negatives stay separate.
- Primary authoring-policy success includes frozen no-package fallback and all failed-creation costs. Generator coverage assigns no usable produced skill zero. Appropriate alternative routing and conditional artifact quality are separately reported. Shared fallback observations must not be counted as independent data.
- Public creators must be pinned and preserved. The current pin file audits selected files, not complete dependency closures. Common-host adaptation excludes unavailable human/native-loop capabilities and must never be represented as native-baseline performance.
- Current workers may inherit background context and access shared files. Fresh conversations, hashes and "do not read" instructions are not access controls. The first pilot is public, exploratory and contaminated by design knowledge; independent confirmation remains blocked without real custody/resources.
- Graders need positive, defective and valid-alternative controls; source-brief prose needs factual review in addition to a valid ledger. Partial traces support observed compliance only, not verified absence of forbidden actions.
- Static/schema/oracle-control tests and runtime comparative tests are different evidence. R5 runs only the former. R6 follows after a fresh checkpoint.

## Important open questions

These do not block writing the initial research candidate:

- Actual host/model/tool identifiers, available telemetry, budget supervision and source-loading behavior need run preflight. Runtime nondeterminism may remain unavoidable.
- Provisional margins (0.90 adequacy, +0.10 worthwhile gain, 0.05 quality-loss/equivalence region and 20% timing reduction) are engineering proposals, not approved universal/user preferences.
- The candidate may lose or add no value over a template/direct solver. The protocol permits that outcome.
- Native comparison, independent custody, competent independent reviewers, realistic prevalence and larger resource commitments remain unproven/unapproved. The conditional 60-brief confirmation plan would require 480 creation policies and 4,320 downstream episodes, far beyond the authorized pilot. It is a resource-gated plan, not a scheduled experiment.
- Anthropic catalog interference remains a statically supported risk with no measured incidence; live concurrency diagnostics are outside the current sequential-work scope.
- Earlier source limits remain: do not turn SkillsBench associations into expected effects; the inaccessible SWE repository is not inspected code; selection/reference-dependence caveats and the unread TMLR final-version limit remain.

## Exact fresh-context prompt for R5

```text
Work on R5 only in GitHub repository danrjoyce/skills, branch research/skill-quality, draft PR #1. Inspect actual remote head and repository guidance before writing. Read AGENTS.md, CLAUDE.md, .agents/invocation.md, projects/skill-quality/README.md, TASKS.md, HANDOFF.md, research/comparative-protocol.md, evaluation-fixtures.md, pilot-manifest.json, evaluation.schema.json, verify-r4.py and verification-r4.md. Read the revised main analysis, R2 critique, R3 response ledger and public implementation audit/pins where needed. Do not rely on earlier private reasoning. If R5 already exists, inspect it rather than duplicate it.

Implement the first research-only standard Agent Skill at projects/skill-quality/candidate/evidence-skill-creator/. It is a model-invocable, host-loaded authoring workflow, not a newly registered native tool or service. Provide SKILL.md, agents/openai.yaml and only justified supporting references/scripts. Keep it uninstalled, unpromoted, and out of existing skill buckets, router, plugin manifests and global host directories. A project-local research package can be loaded explicitly by a later experimental adapter; do not claim native compatibility before testing.

Aim for a lean useful creator, not a copy of the whole research protocol. It should establish the authorized task/use contract, choose a simpler alternative when appropriate, obtain material missing information without routine preference friction, define observable success and safe verification, build minimal reusable resources, validate what can actually be checked, preserve source/version/assumption limits, and report the package/status, actual tests, costs/limits and next steps. Separate creator-policy success from generated-skill performance. Include relevant safety/provenance/failed-generation rules without teaching to the literal final fixture answers. Do not claim a rule is empirically optimal merely because R4 proposes it.

Implement minimal deterministic fixture and record-validation support for the three R4 synthetic families and routing/calibration specifications. Standard-library fixture builders should preserve originals, use safe temporary directories and inert attack text, and produce file inventories, stable IDs and exact case contracts. Implement mechanically decidable oracles and positive/negative/noncanonical controls. Source-brief factual/semantic and incomplete-trace limitations must remain explicit. Validate manifests/attempt records and cross-record semantics, including all failures, fallback links, predicate coverage, costs, caps, unique IDs and exposure records. Keep design/planned rows distinct from measured results. A synthetic trace replay is not a live host observation.

Where baseline source materialization is useful, retrieve only the pinned public OpenAI/Anthropic creator directories and transitive local resources through authorized read-only routes, inventory hashes/licenses/dependencies, and never substitute installed private variants. Do not execute native model CLIs, optimization loops or the creators. Do not silently repair upstream baseline semantics. Defer any unavailable dependency or credential rather than install/provision/spend.

Run deterministic local tests, schema checks, helper tests, fixture/oracle calibration controls and package/static inspection. These tests are allowed, but do not run the candidate or public creators through a model, do not start the comparative pilot, and do not claim runtime compatibility, solver reliability, a calibrated general-purpose grader, isolated holdouts or superiority. Keep runtime adapter design proportional and record which telemetry/isolation guarantees the available environment cannot provide. No paid APIs, new credentials/cloud costs, live external side effects, real sensitive data, security-setting changes, merges or upstream synchronization.

Challenge any protocol inconsistency you find and record a focused correction with rationale before implementing against it; don't silently change task weights, budgets, baselines or primary outcomes. Preserve original protocol/history where a versioned amendment is needed. Keep no-extra-spend exploratory R6 feasible, while resource-gated native/independent confirmation remains separate. Do not block routine R5 implementation on optional user preferences or hypothetical paid resources.

Update README, TASKS, HANDOFF, a candidate design/requirements traceability record and R5 verification. Freeze the candidate and deterministic support at a reviewable checkpoint and write the exact R6 preflight/pilot prompt, including the common-host adaptation, full-source pinning, USD 0 new-spend ceiling, supervisory limits, sequential runs, unknown telemetry, contaminated public fixtures and all-attempt accounting. Publish only the authorized project changes on the existing branch and verify remote bytes, changed-path scope and checks. Keep one substantive task active, no parallel delegates; renew context conservatively around 50,000 to 60,000 tokens and before approximately 90,000. Report exact artifacts/commit, actual checks, failures, and unresolved runtime/resource limits. Stop after R5; do not launch R6 in the same context.
```

## Resume precautions

Publication permission does not authorize spending, installation, external data sharing, security changes or merging. Continue through existing authorized tools; parent verified no usable saved/desktop environment for this task and authorized the cloud fallback. Recheck actual availability if the task needs a different executor. The protocol is ready for implementation, not evidence that every runtime experiment can already run.
