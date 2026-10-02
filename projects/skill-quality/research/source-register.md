# Source register and evidence triage

Research/revision date: **2026-10-02 UTC**. R1 sources were independently revisited for R3; the R2 critique remains unchanged. This is a targeted, critically selected evidence set, not an exhaustive systematic review. Claims are limited to the versions and passages inspected. No published experiment was independently reproduced here.

## How sources are admitted

Authority and empirical support are separate:

- **Normative authority:** a specification determines its own format, not whether following it improves outcomes.
- **Implementation authority:** source code establishes what the inspected implementation does, not how well it generalizes.
- **Methodological support:** conceptual, statistical, or evaluation research justifies an inference or exposes a failure mode. Transfer to skills must be argued.
- **Direct empirical support:** experiments on skills are most relevant to effect size, but selection, controls, uncertainty, and replication constrain what they establish.

Primary sources are preferred. Peer review strengthens scrutiny but does not repair a mismatched population or weak comparator. Recent direct preprints are retained only as provisional evidence with inspectable methods. Marketing, popularity, repository stars, and unattributed summaries are not treated as evidence of superiority.

## S1. Agent Skills specification

- **Source:** [specification at pinned commit](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx)
- **Version:** `69ef37e9424c0a7ea9dd2293b559e43ec8176379`; head captured during R1 on this date, retained as a frozen baseline rather than a promise of the latest future version. File blob `d9a2db099d905da8b879a5c6f996728073985279`.
- **Role:** authoritative format definition. Inspected frontmatter, compatibility, resources, disclosure, and validation sections.
- **Use:** establishes the package contract and runtime-dependent aspects. Its recommendations are not controlled evidence for an optimal length or structure.
- **Limit:** parseability is not behavioral portability, usefulness, or safety.

## S2. OpenAI public skill creator

- **Source:** [SKILL.md](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md), [validator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py)
- **Version:** repository `49f948faa9258a0c61caceaf225e179651397431`; creator blob `72bc0b97e7a6476254a9d5c424c9971748402ec3`; validator blob `0547b4041a5f58fa19892079a114a1df98286406`.
- **Role:** authoritative implementation of this public baseline, not every installed Codex variant.
- **Inspected:** complete creator and validator.
- **Use:** resource planning, progressive disclosure, degree of procedural constraint, validation, iteration.
- **Limit:** no controlled comparative study accompanies the inspected creator. Static checks must not be described as proof of behavioral quality. See the audit for concrete specification/validator discrepancies.

## S3. Anthropic skill creator

- **Source:** [creator directory](https://github.com/anthropics/skills/tree/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator)
- **Version:** repository `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`; creator blob `65b3a402dbd09b8e83f9d637c6b553875189085c`.
- **Inspected:** creator workflow and platform branches; complete `run_loop.py` and `run_eval.py`; relevant grader and comparator instructions.
- **Role:** strong practical baseline with observable evaluation machinery.
- **Use:** paired runs, artifact-grounded grading, human review, trigger evaluation, iterative improvement.
- **Limits:** intended development feedback is different from confirmatory evidence. Platform-specific fallbacks change the available evaluation procedure. Selection is explicitly documented by the authors; the audit does not allege hidden leakage or an unbiased-score claim. Parallel probe interference is a static risk, not an observed error rate. The source's recommendation to encourage triggering is a context-sensitive heuristic, not a universal optimum. The [audit](implementation-audit.md) separates exact code observations from implications.

## S4. Agent Skills output-evaluation guide

- **Source:** [pinned evaluation guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/skill-creation/evaluating-skills.mdx)
- **Version:** file blob `7c90d54295be88ac40de7f19db0876cee6180c4e`.
- **Role:** practical guidance; complete guide inspected.
- **Use:** explicit no-skill comparisons, outcome inspection, timing, iterative diagnosis.
- **Limits:** assertions added after seeing results are development artifacts. Reusing them is not an independent final test. Always-passing safety or preservation checks can still be valuable regression guards, even if they do not discriminate current candidates. The guide's link to the Anthropic creator and overlapping workflow mean these are not independent empirical confirmations.

## S5. Agent Skills client integration guide

- **Source:** [pinned integration guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/client-implementation/adding-skills-support.mdx).
- **Version:** same Agent Skills commit as S1; blob `6c784309faec4ea27715e57734e1e0b5929c1977`, independently retrieved in R2 and R3 and now added to the manifest.
- **Inspected:** discovery/trust, parsing, catalog filtering, activation, paths/resources, and optional delegation.
- **Use:** file access or a host-registered activation tool supplies instructions; user-explicit activation can be injected by the host. Package trust and model-invocation filtering matter.
- **Limit:** integration recommendations describe options, not proof that each host implements them or that a package registers a native function. The guide's broad implementation language is not adopted as a universal portability guarantee. Its lenient-parser advice and the format's strict constraints are distinct contracts.

## M1. Measurement and Fairness

- **Bibliography:** Abigail Z. Jacobs and Hanna Wallach, FAccT 2021. [DOI](https://doi.org/10.1145/3442188.3445901); [inspected arXiv v3](https://arxiv.org/html/1912.05511v3).
- **Inspected:** conceptual setup and sections 3.1-3.2.
- **Role:** peer-reviewed methodological framework for making measurement assumptions explicit.
- **Limit:** fairness-focused conceptual work, not validation of a skill-quality scale. This project's application and decision model remain proposals.

## M2. Model-selection bias

- **Bibliography:** Gavin C. Cawley and Nicola L. C. Talbot, “On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation,” JMLR 11(70), 2079-2107, 2010. [Paper and publication record](https://jmlr.org/papers/v11/cawley10a.html); [PDF](https://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf).
- **Inspected:** abstract, introductory argument, and nested-evaluation discussion.
- **Role:** peer-reviewed empirical and methodological evidence that optimization of noisy selection criteria can bias evaluation.
- **Transfer limit:** not a skill study; it supports the selection/test distinction, not the magnitude of bias in Anthropic's optimizer. That magnitude is unmeasured here.

## M3. AI Agents That Matter

- **Bibliography:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind Narayanan, 2024. [Inspected arXiv v1](https://arxiv.org/html/2407.01502v1).
- **Inspected:** sections 2 and 5, holdout taxonomy, associated methodology passages.
- **Role:** primary experiments and critique of agent evaluation, including cost-sensitive baselines and holdouts appropriate to claimed generality.
- **Limit:** experiments concern earlier agents and benchmarks, not modern skill creators. A later [TMLR record](https://openreview.net/forum?id=Zy4uFzMviZ) was identified in R1/R2, but R3 again received a browser-verification page. The final text is not admitted as inspected evidence. This project cites the accessible pinned preprint; no equivalence with the final publication is assumed. Its general cost/holdout arguments are retained, not its historical performance rankings.

## M4. Interactive information retrieval

- **Bibliography:** Pia Borlund, “The IIR evaluation model: a framework for evaluation of interactive information retrieval systems,” Information Research 8(3), paper 152, 2003. [Full text](https://informationr.net/ir/8-3/paper152.html).
- **Inspected:** framework, simulated work-task situations, and recommendations.
- **Role:** original evaluation framework connecting relevance judgments to tasks and context.
- **Limit:** human retrieval studies are not agent-skill experiments. The paper's inference from non-significant differences to equivalence is not adopted. We use its contextual evaluation idea, not a claim that simulations and real users are interchangeable.

## E1. Tau-bench

- **Bibliography:** Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan, 2024. [Inspected arXiv v1](https://arxiv.org/html/2406.12045v1).
- **Inspected:** task/reward definition, `pass^k` versus `pass@k`, construction.
- **Role:** primary reliability methodology for interactive tool agents.
- **Limit:** simulated users and limited domains; endpoint rewards do not fully verify authorization. No current-model ranking is inferred.

## E2. AgentDojo

- **Bibliography:** Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, and Florian Tramèr, NeurIPS 2024 Datasets and Benchmarks. [Proceedings record](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html); [inspected early method version](https://arxiv.org/html/2406.13352v1).
- **Inspected:** stateful environment, user and attacker goals, utility/security framing.
- **Role:** primary experimental framework for prompt-injection evaluation.
- **Limit:** threat models, tasks, and attacks are bounded. Its results do not certify any package or establish current attack/defense rates. No numerical result is transferred here.

## E3. LLM-as-a-judge

- **Bibliography:** Lianmin Zheng and colleagues, “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena,” NeurIPS 2023 Datasets and Benchmarks. [Proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html); [inspected arXiv v4](https://arxiv.org/html/2306.05685v4).
- **Inspected:** bias experiments and order-swap analysis.
- **Role:** primary evidence of judge strengths and failure modes.
- **Limit:** conversational preference evaluation with older models, not validation of a current artifact grader. Agreement with humans is not identical to factual correctness. Calibration must be task-specific.

## E4. Test-set contamination

- **Bibliography:** Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, and Tatsunori B. Hashimoto, “Proving Test Set Contamination in Black Box Language Models.” [Inspected arXiv v2](https://arxiv.org/html/2310.17623v2), associated with ICLR 2024.
- **Inspected:** method summary and section 6 limitations.
- **Role:** primary statistical method with explicit assumptions.
- **Limit:** needs likelihood access and an appropriate exchangeability argument; does not rule out all partial or indirect contamination. An absent detection is not proof of an uncontaminated benchmark.

## D1. SkillsBench

- **Bibliography/status:** Xiangyi Li and colleagues, 2026, primary preprint. [Version history](https://arxiv.org/abs/2602.12670), [historical v1](https://arxiv.org/html/2602.12670v1), [current v4](https://arxiv.org/html/2602.12670v4). Peer-review status not established here.
- **Historical v1 (13 February 2026):** R1 inspected sections 2-5 and appendices; 86 constructed/84 evaluated tasks, seven configurations, reported +16.2 percentage points. Retained as a historical account, not the current aggregate or an independent replication.
- **v4 (14 June 2026):** R3 inspected sections 3-5 and appendices D.6, G, N. Reports 87 tasks, 18 configurations, 33.9% versus 50.5% (+16.6 points), with three selected trials per cell. Construction rejects low-separation tasks. Healthy scored runs precede timeout backfills; other coverage gaps are rerun. Plotted intervals use result-count Wald calculations. Generated-skill protocols differ in reuse/isolation and report discovery/interference problems.
- **Our inference:** these choices define a selected benchmark intervention, not prevalence-weighted first-attempt deployment value. Excluding some timeouts can remove treatment-mediated cost; direction/magnitude cannot be established without all attempts and causes. Result-count intervals do not supply a paired, task-clustered effect interval. Better coverage and recency do not remove those limits.
- **Disposition:** retain descriptive experimental evidence and design hypotheses; exclude pooled version estimates, a causal package-size optimum, universal deployment gains, and rankings of the exact pinned creators. R4 may use benchmark tasks as disclosed development material, not secretly repurpose public cases as a sealed test. No raw-run reproduction here.

## D2. SWE-Skills-Bench

- **Bibliography/status:** Tingxu Han and colleagues, 2026. [Inspected arXiv v1](https://arxiv.org/html/2603.15401v1), sections 3-4 and equation 5. Primary preprint; peer-review status not established here.
- **Observed:** 49 skills/565 instances, one Claude Code/Haiku 4.5 configuration, reported approximately +1.2 points with a high baseline. Sections 3.2 and 4.1 give different placement accounts. No repetition protocol was identified in inspected text. The linked [repository](https://github.com/GeniusHTX/SWE-Skills-Bench) returned 404 in R2 and R3's GitHub API check; loading and raw trials remain unverified. No reason for the 404 is inferred.
- **Metric:** equation 5 divides accuracy change by relative token-cost change. Our algebraic counterexample: +0.02 accuracy and -0.10 cost gives -0.2, although both improve; -0.02 accuracy and -0.10 cost gives +0.2 despite lower accuracy. Zero cost change is undefined. These are illustrations, not paper data.
- **Disposition:** retain a qualified reported observation and verification lead. Exclude that ratio as an overall value rule, near-null-as-equivalence claims, and calibration of this project's expected effect or budget. Accessible paper text supports this restricted use; inaccessible code does not support any code claim. Access plus a loading/data audit would be required to upgrade it.

## D3. SkillLearnBench

- **Bibliography/status:** Shanshan Zhong and colleagues, 2026. [Inspected arXiv v1](https://arxiv.org/html/2604.20087v1), sections 3-4 and appendices K-M. Primary preprint; peer-review status not established here.
- **Observed:** 20 tasks/100 instances selected for skill dependence, 17 tasks adapted from SkillsBench, fixed solver, and a single-round Skill-Creator condition. Artifact/trajectory scores depend on references and oracle steps. Appendix L.3 reruns the judge on fixed outputs; this is evaluator repeatability evidence rather than solver reliability.
- **Our inference:** efficient valid alternatives can differ from an oracle sequence. Stable grading does not prove valid grading, and textual safety judgments cannot establish behavior under attack. Shared task origins constrain independence of evidence.
- **Disposition:** retain for hypotheses about authoring feedback and metric design. Exclude full-workflow creator ranking, behavioral safety certification, and any implication that one generation or solver trial suffices for general comparative inference. R4 must independently calibrate its own oracles and estimate relevant variance.

## Claim-level admission summary

| Sources | Retain for this claim | Exclude or defer this inference |
|---|---|---|
| S1, S5 | Format and proposed integration contracts | Runtime compatibility, native-tool registration by a file, or demonstrated benefit without execution |
| S2, S3 | Exact public construction workflows and inspected code paths | Comparative creator quality, deployed error frequency, or concealed intent |
| S4 | Practical evaluation design ideas | Independent outcome replication or always-passing invariants being dispensable |
| M1 | Explicit measurement assumptions | A validated latent skill-quality scale; technical psychometric terms for our custom checklist |
| M2 | Selection-bias mechanism and need for valid post-selection inference | Measured bias in the pinned optimizer or a claim its authors never made |
| M3 inspected preprint | Cost-aware baselines and holdout scope | Unread final-version claims or current-model performance |
| M4 | Contextual relevance analogy | Agent activation validation or nonsignificance as equivalence |
| E1 | Reliability distinction and endpoint/process gap | Current skill failure rates or independent-run formulas for stateful retries |
| E2 | Joint benign utility and adversarial evaluation under a threat model | Certification or extrapolation to untested attacks/hosts |
| E3 | Judge-bias mechanisms | Validity of this project's uncalibrated grader |
| E4 | Bounded contamination-detection argument | Proof of cleanliness from a negative detector result |
| D1-D3 | Qualified reported experiments and hypotheses, with dispositions above | Universal effectiveness/ineffectiveness, a pooled effect, or superiority of a new creator |

**Evidence status:** paper-reported results, source-code observations, and this project's proposals remain separate. No source has been independently reproduced by this project. Important framework claims survive removing D1-D3: their justification is the stated counterexamples, runtime contracts, and methodological arguments, not a borrowed headline.

## Screened but not used as load-bearing evidence

- Recent agent-skill surveys and ecosystem catalogs: useful discovery leads, but secondary or primarily descriptive. They do not replace the inspected primary methods.
- Skill “quality” rankings based on stars, format completeness, or static LLM ratings: no demonstrated causal relationship to downstream benefit in the reviewed material.
- General lists of prompting tips, vendor marketing, social-media summaries, and unattributed benchmark claims: excluded from support for substantive conclusions.
- Human psychological-test studies: cautionary but less direct than the admitted measurement framework; not imported as an agent-skill score.
- The live OpenAI skills documentation URL redirected to ChatGPT Learn during retrieval. No detailed claim rests on that mutable page; the public code baseline is pinned instead.

## Evidence gaps that must survive the handoff

1. No direct comparison of the exact pinned OpenAI and Anthropic creators under a matched protocol has been established here.
2. No independent reproduction of the three direct skill benchmarks has been done.
3. Cross-harness discovery, permission behavior, and package compatibility need runtime testing.
4. Static quality dimensions need criterion validation against downstream utility; intuitive plausibility is insufficient.
5. There is no empirically justified universal pass rate, sample size, entrypoint length, or number of modules.
6. The project needs domain judgment about intended use and risk before choosing release thresholds.
