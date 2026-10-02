# Research handoff

Updated: **2026-10-02 UTC**.

## Current state

**R1 foundations, R2 independent critique, and R3 conceptual revision are complete. R4 comparative-protocol design is next.** Continue on `research/skill-quality` and [draft PR #1](https://github.com/danrjoyce/skills/pull/1), based on main at `3cca18b368ae95cdbdebbff572ccafa662551015`. Inspect the actual branch tip before writing; do not recreate the branch or PR.

R1's substantive draft was published at `abbb267774acafdb8cfaad70b7b8dea3b1ae8f27`, with tracking checkpoint `9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8`. R2's critique is at `ca27f690562c7440458dc50cdc0f01b5073f08ad`. R3 revised from that commit and preserves the independent critique and historical R1 verification unchanged. The PR and [R3 verification record](research/verification-r3.md) identify the published revision checkpoint.

No final creator, model-performance experiment, runtime compatibility result, calibrated grader, sealed holdout, or superiority finding exists. The conceptual framework is settled enough for protocol design; numerical thresholds, actual host configurations, budget, and custody remain open. No merge, repository-security change, or upstream synchronization is part of this checkpoint.

## Read these artifacts

1. [Revised main analysis](how-to-determine-if-a-skill-is-good.md), especially sections 1.2-1.4, 2.3, 3, 6.4, 7, 9-11
2. [R3 response ledger](research/revision-01.md), C1-C9 dispositions and limits
3. [Independent R2 critique](research/critique-01.md), preserved unchanged
4. [Source register](research/source-register.md), exact versions and claim-level admission
5. [Static implementation audit](research/implementation-audit.md), including unexecuted instrument qualification plan
6. [Implementation pins](research/implementation-pins.json), ten independently rechecked public files
7. [Methodology](research/methodology.md), historical R1 process and R3 rechecks
8. [Task ledger](TASKS.md) and [R3 verification](research/verification-r3.md)

## Decisions to preserve

- Fitness for purpose, incremental value, adoption, and superiority are different. Equal adequate alternatives can both be good; nonsignificance is not equivalence.
- The initial candidate is a host-loaded model-invocable authoring workflow, not a registered native service. Claude Code/Codex are intended targets, untested. A host/adapter supplies discovery, loading, execution, permissions, and results. Generated user-only artifacts require explicit-invocation evaluation.
- Distinguish package deployment effect, forced-use diagnostics, and component mechanisms. Skill access traces do not establish understanding or causal benefit.
- The complete creator policy includes all attempts, human help, budgets, selection, status/fallback handling, and adapter. Broader authoring value and conditional/production skill quality are separate claims.
- Freeze the creator before evaluation-family adaptation, then freeze each artifact before downstream confirmation. The solver sees its legitimate task/input; solutions/grader secrets remain concealed. No actual custody boundary exists yet.
- Use observable outcome/process checks, evaluator repeatability and substantive validity, and separate solver reliability. Critical false passes cannot be averaged away.
- Evaluation should be proportionate: development, bounded adoption, and comparative research are different tiers. Include prospective human time, all-traffic catalog overhead, maintenance, failures, and retirement without charging each skill for the whole research project.
- Operational timeouts and budget overruns are outcomes. Distinguish external outage, ambiguous missingness, and oracle failure; keep all attempts and rerun links. Match uncertainty to episodes, artifacts, briefs, and families.
- Preserve hard authorization/safety constraints across creator references, package/dependencies, execution, and graders. Use inert fixtures and controlled sinks; report benign utility alongside attack outcomes.

## Evidence cautions that must survive

- Source register D1 reconciles historical SkillsBench v1 with current v4. Neither versions nor shared benchmark tasks are independent replications. Selection and uncertainty limitations prevent importing a headline as expected deployment benefit or ranking these exact creator implementations.
- D2's accessible paper is a qualified lead. The linked SWE repository still returned 404 in R3; loading/raw trials are unverified. Its ratio is not an admissible general cost-quality rule.
- D3 is useful process evidence with selection/reference dependence and an adapted creator. Judge repeatability does not establish behavioral safety or solver reliability.
- Anthropic's authors explicitly describe validation selection and withhold that feedback from the improvement prompt. Do not invent hidden leakage or an unbiased-score claim. Independent confirmation or justified selection-aware inference is needed for the project's additional generalization claim.
- Concurrent probe catalog interference is a statically supported risk with no measured incidence/effect. Preserve native baseline fidelity. A repair changing creator feedback is a separately labeled method; a common external evaluator may assess frozen artifacts.
- The TMLR final text for M3 remains unread due to browser verification. Use the inspected pinned preprint for bounded methodology, not assumed final-version equivalence.

## R4 decisions and owners

| Decision | Required evidence or owner | If unavailable |
|---|---|---|
| Target creation families, prevalence, primary authoring/generator claim | User's intended use and research rationale | Propose explicit options; do not claim deployment representativeness |
| Native call interface versus host-loaded workflow | Actual use contract; user if materially changed | Retain R3 scope with a pending decision |
| Host/model/tool versions and baseline fidelity | Available authorized environments and public implementations | Document requirements and untested status; no simulated claim of execution |
| Budget, horizon, adequacy, practical margins, critical harms | User/domain owner; scoped proposals can be researched | Mark pending approval/value choice; no paid calls |
| Holdout custody and access enforcement | Real authorized custodian/environment and access controls | Exploratory public evaluation with correspondingly limited claims |
| Sample allocation, repetitions, uncertainty, stopping | Pilot variance and feasible cost; analyst rationale | Design a bounded pilot, not arbitrary universal sample counts |
| Grader calibration and human feedback | Validated fixtures, expertise availability, fair help policy | Narrow supported tasks or label measurement unqualified |

R4 should complete a concrete proposed protocol and expose approval gates. It need not pretend every prerequisite exists to finish its design artifact. R5 implementation must wait for an adequately specified protocol and any material scope/resource decisions.

## Exact fresh-context prompt for R4

```text
Work on R4 only in GitHub repository danrjoyce/skills, branch research/skill-quality, draft PR #1. Inspect the current remote branch and repository guidance before writing. Read AGENTS.md, CLAUDE.md, .agents/invocation.md, projects/skill-quality/README.md, TASKS.md, HANDOFF.md, the revised main analysis, research/revision-01.md, research/critique-01.md, and supporting source/audit/methodology/pin/verification records. Do not rely on prior private reasoning. If R4 already exists, read it and current status rather than duplicating it.

Design the comparative evaluation before implementing a creator. First challenge the R3 framework's practical assumptions, especially its initial host-loaded callable contract, broader authoring-value versus generator-quality estimands, fallback scoring, paired/nested design, and real information boundary. Record any correction with evidence, not automatic agreement.

Produce research/comparative-protocol.md with a concrete proposed primary claim and outcome, creation-family and downstream-task sampling frame, weights and units, strong baselines, faithful native versus adapted comparison labels, permissions/catalog/host requirements, creation and execution budgets, human clarification/feedback policy, all-attempt selection/failure/abstention accounting, and prospective cost horizon. Explain why selected families and comparators answer the user's aim. Keep user/domain value decisions and spending approvals explicit; do not invent them.

Specify the staged information-flow and actual holdout custody requirement, what each creator/solver/evaluator may see, artifact/method freeze points, contamination/reset checks, and an exploratory fallback if independent custody cannot be established. Publicly inspected tasks cannot be described as a sealed holdout. Do not publish future secret cases or answers in this public repository.

Define metric/oracle and trace contracts, deterministic and human/LLM grader calibration, critical false-pass tests, noncanonical valid solutions, delayed/substituted/user-only activation cases, benign/adversarial threat-model pairs, unsupported hosts, and severe noncompensating gates. Turn the Anthropic probe audit into a diagnostic plan preserving the native baseline; label any repaired feedback path as a different method. No empirical risk frequency is known yet.

Write explicit timeout/outage/unknown/oracle-failure and rerun rules; an attempt-ledger schema; paired/nested weighting and clustering; treatment of failed creation and unsupported outputs; intended confidence/decision regions for superiority, noninferiority, equivalence, or quality-cost tradeoff; a finite claim/multiplicity family; and a stopping rule that accounts for adaptive development. Propose a risk-proportionate pilot/variance and budget-sizing plan before choosing expensive sample counts. Use worked planning arithmetic where useful, labeled illustrative, and distinguish finite-suite from transported population claims.

Include a go/no-go checklist and list the remaining user/resource/custody decisions that block an actual run. R4 is design only: no candidate skill implementation, paid model/benchmark run, real secret/destructive test, shipped-skill edit, repository-security change, merge, or bulk upstream sync. Safe local document/schema/arithmetic checks are allowed. Do not change frozen public baselines or historical critique records silently.

Update README, TASKS, HANDOFF, and a verification record. End with a precise R5 prompt if the protocol is sufficiently specified, or a narrowly scoped prerequisite task if it is not. Publish on the existing branch and verify remote bytes, changed-file scope, links/anchors, JSON/schema examples, and arithmetic. Keep one substantive task active, no parallel research workers, and renew context conservatively around 50,000 to 60,000 tokens and before approximately 90,000. Report the artifact, verified commit/links, consequential design choices, unresolved approvals, and verification limits.
```

## Resume precautions

Read-only source research does not imply permission for new credentials, paid experiments, private-data sharing, repository settings, or merging. Use existing authorized connectors/environments and check actual availability. Distinguish a design ready for review from a run ready to execute. Do not treat the parent task's publication permission as authority to spend or deploy.
