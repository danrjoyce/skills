# Research handoff

Updated: **2026-10-02 UTC**.

## Current state

**R1 foundations and R2 independent critique are complete. R3 revision is next.** Continue on `research/skill-quality` and [draft PR #1](https://github.com/danrjoyce/skills/pull/1), based on main at `3cca18b368ae95cdbdebbff572ccafa662551015`. Inspect the actual branch tip before writing; do not recreate the branch or PR.

R1's substantive draft was published at `abbb267774acafdb8cfaad70b7b8dea3b1ae8f27`; its tracking checkpoint was `9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8`. R2 reviewed that checkpoint in fresh context. Its deliverable is [critique-01.md](research/critique-01.md), approximately 5,300 words. R2 adds the critique and updates TASKS, HANDOFF, and README only. The main analysis and R1 evidence artifacts remain unchanged so the criticism and subsequent response are auditable separately.

The project is research documentation only. No final meta-skill, performance benchmark, sealed holdout, runtime compatibility test, or superiority result exists. No merge, repository-security change, or upstream synchronization is part of this project checkpoint.

## Artifacts

1. [Main analysis](how-to-determine-if-a-skill-is-good.md), still the R1 draft
2. [Independent critique](research/critique-01.md), the R2 deliverable and acceptance checklist
3. [Source register](research/source-register.md), awaiting the R3 dispositions and version reconciliation
4. [Pinned implementation audit](research/implementation-audit.md), awaiting the R3 corrections
5. [Source-version manifest](research/implementation-pins.json)
6. [Methodology and limitations](research/methodology.md)
7. [Task ledger](TASKS.md)
8. [R1 verification record](research/verification-r1.md)

## Findings to preserve and resolve

The critique retains the relational view of quality, the separation of deployment/forced-use/ablation experiments, the distinction between implementation evidence and outcome evidence, and the draft's arithmetic. Its required changes are identified as C1-C9:

- **C1:** distinguish fitness for purpose, incremental value, adoption, and comparative superiority. The definition should admit equally good alternatives.
- **C2:** specify the callable deliverable and supported runtime contract. A skill package does not itself register a native tool. Respect the distinction between user-only and model-driven invocation.
- **C3:** reconcile SkillsBench v4, dated 14 June 2026, rather than presenting v1 as the whole current evidence picture. Scrutinize run selection and inferential claims; the new headline is not automatically stronger evidence. SWE-Skills-Bench's cost-efficiency ratio has a sign problem, and its linked repository returned 404 through web and GitHub API reads. SkillLearnBench remains a qualified process study, not a full-creator ranking.
- **C4:** the Anthropic optimizer really selects on its held-out split. Its authors explicitly describe this as a development selection procedure; do not imply concealed leakage or an unbiased-generalization claim they did not make. The shared command directory creates a static concurrent-probe interference risk; runtime frequency is unknown. Preserve baseline fidelity and separate any repaired-harness diagnostic.
- **C5:** define skill- and creator-level estimands, failures, abstention, feedback, selection, analysis units, and staged information access.
- **C6:** distinguish observable access/action events from understanding; distinguish evaluator repeatability and validity from solver reliability.
- **C7:** introduce proportionate evaluation tiers and a coherent prospective cost boundary, including catalog overhead and human effort.
- **C8:** predeclare how timeouts, reruns, clustering, margins, and adaptive selection affect claims. A non-significant difference is not equivalence.
- **C9:** include the creator and package supply chain in the threat model; test useful benign behavior as well as resistance to attacks.

All nine implementation-file blob pins in the R1 manifest matched independently fetched public files. The new pinned integration guide is `docs/client-implementation/adding-skills-support.mdx` at Agent Skills commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379`, blob `6c784309faec4ea27715e57734e1e0b5929c1977`. The critique contains direct links and code anchors.

These are review findings, not instructions to agree automatically. R3 must either make a justified revision, rebut an item with evidence, or explicitly defer an empirical question to its proper stage. No measured effect size exists for the newly identified probe risk.

## Exact fresh-context prompt for the next substantive task

```text
Work on R3 only in GitHub repository danrjoyce/skills, branch research/skill-quality, draft PR #1. Inspect the current branch and repository guidance before writing. Read AGENTS.md, CLAUDE.md, .agents/invocation.md, projects/skill-quality/README.md, TASKS.md, HANDOFF.md, research/critique-01.md, the main analysis, and supporting evidence artifacts. Do not rely on the prior author's private reasoning.

Revise the foundations in response to critique C1-C9. Begin by resolving the distinction between fitness, usefulness, adoption, and superiority, and by declaring the initial callable product and supported runtime assumptions. A skill package does not automatically register a native function or MCP tool. Keep repository invocation conventions separate from claims about all hosts.

Reconcile current primary evidence, including SkillsBench v4 versus the historical v1 account. Preserve version-specific claims and qualify run-selection and uncertainty limitations. Do not turn source-code observations, preprints, inaccessible implementation evidence, or reference-similarity scores into replicated outcome evidence. Treat the Anthropic selection procedure fairly: confirm the code, credit its intended training-feedback separation, and distinguish validation selection from final generalization. Record the static shared-catalog probe risk and its unmeasured practical effect without silently modifying or handicapping the baseline.

Write a response ledger in research/revision-01.md for every C1-C9 item: accepted and revised, rejected with evidence, or deferred with a named next step. Revise how-to-determine-if-a-skill-is-good.md and supporting source/audit/methodology records as needed. Formalize the skill and creator estimands, failure and abstention treatment, information boundary, observable metrics, evaluator calibration, proportionate evaluation tiers, cost perspective, missing-data logic, and threat model. Use the critique's checkable acceptance criteria. Keep any unresolved decisions visible rather than choosing arbitrary universal thresholds.

R3 should settle a defensible initial measurement and decision framework, not run the full experiment. Do not implement the final meta-skill, invent a sealed holdout, run paid model experiments without the required authority, edit shipped skills or repository settings, merge, or bulk-sync upstream. Update README, TASKS, and HANDOFF with the revised artifacts and a precise R4 comparative-protocol prompt. Publish sequentially on the existing branch and verify remote bytes and changed-file scope.

Keep one substantive task active. Do not start parallel research workers. Renew context conservatively around 50,000 to 60,000 tokens and before approximately 90,000; stop earlier at a coherent checkpoint. Report the revised artifacts and commit, material changes, remaining empirical and value decisions, verification limits, and the exact next task.
```

## Resume precautions

Compare the current remote PR and branch with this handoff before writing. If R3 already exists, read its response ledger and current task status rather than duplicating it. Preserve the critique as the independent record; corrections to the main argument belong in the revision and its response ledger.

Read-only inspection and source research do not imply permission to change security, create persistent credentials, or merge the PR. If a later experimental step needs money, private data, additional access, or a value judgment that the sources cannot supply, identify the exact decision and continue independent authorized work.
