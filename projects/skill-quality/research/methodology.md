# Research methodology and limitations

Date: **2026-10-02 UTC**. Scope: first foundations chunk, R1.

## 1. Questions and stopping condition

The question is not which creator has the most features. It is what evidence could justify saying that a skill is good, and eventually that one creation process produces better skills than relevant alternatives.

R1 stops when there is:

- A substantive initial answer with an explicit construct and measurement argument
- Primary evidence for the main methodological risks
- Pinned, inspected public creator implementations
- A source-quality record distinguishing authority from empirical support
- A proposed evaluation approach, clearly separated from executed experiments
- A durable handoff for an independent critic

It does not require an exhaustive literature survey, a runnable benchmark, a final creator, or a superiority result. Those are later tasks. The coherence of this boundary matters more than collecting every related paper.

## 2. Retrieval and source-selection process

### Repository and implementation inspection

1. Inspected `danrjoyce/skills` root, branch list, open pull requests, recursive tree, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, and `package.json` at `3cca18b368ae95cdbdebbff572ccafa662551015`.
2. Confirmed no existing research project or competing branch before creating `research/skill-quality`.
3. Retrieved current heads of `openai/skills`, `anthropics/skills`, and `agentskills/agentskills` using GitHub's commits endpoint.
4. Read the relevant files at those immutable commits, not moving `main` links. Recorded repository and blob SHAs in [implementation-pins.json](implementation-pins.json).
5. Examined implementation behavior statically. No creator, trigger optimizer, or public benchmark was run.

The research directory is outside `skills/`, so it is not a shipped skill. The existing plugin manifests, bucket documentation, router, and versioning were not changed.

### Literature searches

Representative queries used during the pass:

- `Jacobs Wallach Measurement and Fairness 2021 construct validity arxiv`
- `Cawley Talbot On Over-fitting in Model Selection Subsequent Selection Bias Performance Evaluation 2010 JMLR`
- `AI Agents That Matter 2024 Kapoor evaluation cost holdout arxiv`
- `tau bench benchmark tool agent user interaction reliability pass k arxiv 2024`
- `AgentDojo dynamic environment evaluating prompt injection attacks defenses`
- `Judging LLM as a Judge MT Bench Chatbot Arena NeurIPS 2023 position verbosity bias`
- `Proving Test Set Contamination in Black Box Language Models Oren 2024 ICLR`
- `agent skills evaluation SkillsBench benchmark skills 2026`
- `agent procedural skills benchmark language model skills skill creator evaluation`
- `The concept of relevance in IR 2003 Borlund DOI`
- `Evaluating interactive information retrieval systems Borlund 2003 simulated work task`

Search results were discovery aids. Load-bearing claims were checked in primary papers, publisher records, or the public code. Search-engine relative publication ages were not used as bibliographic dates. Exact arXiv versions and repository SHAs are recorded instead.

The search was targeted and judgmental. There is no claim of database exhaustiveness, a registered review protocol, complete citation coverage, or an unbiased sample of the literature. Recent surveys were considered as leads rather than as substitutes for primary evidence.

## 3. Admission and exclusion rules

A source was retained if it answered a specific question better than available alternatives and its claim could be bounded responsibly:

- Format and implementation questions: the originating specification or source code
- Measurement and selection-bias questions: established methodological research
- Agent reliability and security questions: primary, inspectable evaluation methods
- Direct skill effects: the most relevant located primary experiments, with preprint status and design limitations explicit

The direct empirical set includes recent preprints because excluding them solely for lack of established peer-review status would remove the most task-relevant evidence. They are not promoted to universal facts or treated as independent replications. No conclusion relies on a single headline number.

Excluded as proof: popularity, commercial claims, blog summaries, static quality rankings without behavioral validation, and generic analogies that do not survive examination. The [source register](source-register.md) documents the main exclusions and remaining gaps.

## 4. How claims were handled

### Evidence versus synthesis

Source observations use narrow language: “the code selects,” “the paper reports,” or “the specification permits.” The proposed definition of quality, decision framework, worked example, and future experimental plan are this project's synthesis. They have not been empirically validated.

Claims of absence are bounded. For example, “no repeated-run protocol identified in the inspected text” does not mean no repetitions occurred. A code path that could conflate an error with abstention is not evidence about how often that happens.

### Causal and inferential caution

The analysis distinguishes total package value from effects of particular components. Cross-task associations between length and outcomes do not establish what would happen if the same skill were shortened. A selected maximum on a validation set does not have the same inferential status as a frozen candidate evaluated independently.

The three direct skill studies differ in task selection, model/harness, intervention, baseline competence, and creator procedure. They are not combined in a meta-analysis. Such pooling would require compatible estimands and accessible trial-level data that this pass did not establish.

### Quantitative examples

Only arithmetic illustrations were calculated locally:

- Activation precision under 1% relevance prevalence, 90% recall, and 5% false-positive rate: `0.009 / (0.009 + 0.0495) = 0.153846...`.
- Zero-failure one-sided bounds under independent identically distributed Bernoulli trials: `1 - 0.05^(1/n)` for `n = 20, 100, 300`.

These calculations test the examples' arithmetic. They are not observations about any skill, model, or user. No paid model evaluation, new credential, or private dataset was used.

## 5. Verification performed and not performed

### Performed in this chunk

- Retrieved public implementation files and pinned their source SHAs
- Checked the relevant code branches behind the consequential implementation critique
- Inspected source sections supporting measurement, reliability, contamination, and direct-study caveats
- Checked illustrative arithmetic
- Checked local research links, source IDs, JSON syntax, repository prose rules, and changed-file scope before publication
- Verified published research bytes and changed paths through the GitHub connector after committing, as recorded in the final checkpoint

### Not performed

- Running or comparing either creator
- Executing the public validators or trigger probes
- Replicating any published experiment
- Validating the proposed quality construct against real deployment outcomes
- Runtime testing across Codex, Claude Code, or other harnesses
- Inspecting every file of the cited benchmark repositories
- Creating or sealing a final holdout set
- Establishing repository branch protection

The draft's static audit and literature analysis should not be described as a benchmark result or a security certification.

## 6. Risks in this draft itself

The independent critic should consider, rather than assume away:

1. The definition may be too demanding for low-risk skills or too broad to operationalize cheaply.
2. The proposed quality dimensions may overlap or omit a critical dimension.
3. Utility weights and hard constraints may hide unresolved normative choices.
4. An overly elaborate evaluation process could lose to a simpler creator once lifecycle cost is counted.
5. Suggested isolation, blinding, and holdout arrangements may be infeasible in a practical call-tool environment.
6. The causal interpretation may require stronger design assumptions than the prose makes clear.
7. The selected literature could reflect search and author judgment rather than the full range of high-quality counterevidence.

These are review questions, not resolved defects or instructions to reach a particular verdict.

## 7. What must be decided later

Before R4 can freeze an experimental protocol, establish target creation families, supported execution environments, acceptable risk, budget, baseline fidelity, who can maintain an inaccessible final set, and how human judgments will be obtained and calibrated. Some facts can be discovered from the repository; value judgments and consequential new resource commitments require an explicit decision.

Keep these unresolved matters visible. Do not substitute arbitrary “industry-standard” thresholds or a few self-generated examples merely to move on to implementation.
