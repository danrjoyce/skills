# Source register and evidence triage

Research date: **2026-10-02 UTC**. This is a targeted, critically selected evidence set, not an exhaustive systematic review. Claims are limited to the versions and passages inspected. No published experiment was independently reproduced here.

## How sources are admitted

Authority and empirical support are separate:

- **Normative authority:** a specification determines its own format, not whether following it improves outcomes.
- **Implementation authority:** source code establishes what the inspected implementation does, not how well it generalizes.
- **Methodological support:** conceptual, statistical, or evaluation research justifies an inference or exposes a failure mode. Transfer to skills must be argued.
- **Direct empirical support:** experiments on skills are most relevant to effect size, but selection, controls, uncertainty, and replication constrain what they establish.

Primary sources are preferred. Peer review strengthens scrutiny but does not repair a mismatched population or weak comparator. Recent direct preprints are retained only as provisional evidence with inspectable methods. Marketing, popularity, repository stars, and unattributed summaries are not treated as evidence of superiority.

## S1. Agent Skills specification

- **Source:** [specification at pinned commit](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx)
- **Version:** `69ef37e9424c0a7ea9dd2293b559e43ec8176379`; current repository head retrieved on the research date. File blob `d9a2db099d905da8b879a5c6f996728073985279`.
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
- **Limits:** intended development feedback is different from confirmatory evidence. Platform-specific fallbacks change rigor. The source's recommendation to encourage triggering is a context-sensitive heuristic, not a universal optimum. The [audit](implementation-audit.md) separates exact code observations from implications.

## S4. Agent Skills output-evaluation guide

- **Source:** [pinned evaluation guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/skill-creation/evaluating-skills.mdx)
- **Version:** file blob `7c90d54295be88ac40de7f19db0876cee6180c4e`.
- **Role:** practical guidance; complete guide inspected.
- **Use:** explicit no-skill comparisons, outcome inspection, timing, iterative diagnosis.
- **Limits:** assertions added after seeing results are development artifacts. Reusing them is not an independent final test. Always-passing safety or preservation checks can still be valuable regression guards, even if they do not discriminate current candidates. The guide's link to the Anthropic creator and overlapping workflow mean these are not independent empirical confirmations.

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
- **Limit:** experiments concern earlier agents and benchmarks, not modern skill creators. A later TMLR record was found, but its full text was blocked in this session; this project cites the accessible pinned preprint, not an assumed identical revision.

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

- **Bibliography:** Xiangyi Li and colleagues, 2026. [Inspected arXiv v1](https://arxiv.org/html/2602.12670v1).
- **Status:** primary preprint; peer-review status not established in this pass.
- **Inspected:** sections 2-5 and appendices C.10, E, F, and relevant failure/exclusion details.
- **Strength:** controlled skill/no-skill conditions, multiple harness-model combinations, repeated trials, deterministic verifiers.
- **Limit:** 86 constructed tasks but 84 evaluated; curated task-skill pairing is an optimistic deployment setting. Missing length-matched and component controls limit mechanism claims. Package-size comparisons stratify different tasks, so confounding prevents a universal “two or three modules is best” prescription. Its own limitations acknowledge important transfer and causal-control gaps.

## D2. SWE-Skills-Bench

- **Bibliography:** Tingxu Han and colleagues, 2026. [Inspected arXiv v1](https://arxiv.org/html/2603.15401v1).
- **Status:** primary preprint; peer-review status not established in this pass.
- **Inspected:** construction, experimental setup, metrics, and results.
- **Strength:** pinned repositories, explicit acceptance criteria, paired comparisons, cost reporting.
- **Limit:** filters toward feasible, deterministically testable tasks; one Claude Code/Haiku 4.5 solver configuration. Section 3.2 describes placement under `~/.claude`; section 4.1 says project root. No repeated-run protocol was identified in the inspected text. These uncertainties constrain reuse and interpretation; they are not evidence of invalid results. Actual loading and raw trials need independent code-level audit.

## D3. SkillLearnBench

- **Bibliography:** Shanshan Zhong and colleagues, 2026. [Inspected arXiv v1](https://arxiv.org/html/2604.20087v1).
- **Status:** primary preprint; peer-review status not established in this pass.
- **Inspected:** sections 3-4 and appendices K, L, M excerpts.
- **Strength:** directly evaluates skill generation and downstream execution while fixing the solver.
- **Limit:** 20 tasks and 100 instances, explicitly selected for low no-skill success and solvability with human skills. Seventeen tasks derive from SkillsBench, so the studies are not independent samples. Judge-based artifact and trajectory scores depend on reference/oracle choices. The single-round creator adaptation cannot rank the complete current Anthropic workflow. Useful for hypotheses and protocol design, not broad superiority conclusions.

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
