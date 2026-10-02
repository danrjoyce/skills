# How to determine if a skill is good

**Status:** first research draft, 2026-10-02. Independent criticism and revision are still required. No skill-performance experiment was run for this project. Numerical examples below are illustrative calculations, not results.

## The answer in one paragraph

A good skill is a **reusable intervention that helps a specified agent achieve legitimate user goals, in a specified environment and task distribution, more reliably or economically than the best relevant alternative, without unacceptable side effects**. Its quality is established by a defensible comparison of behavior and outcomes, not inferred from polished instructions, format compliance, apparent comprehensiveness, or the authority of its author. Selection, execution, verification, and maintenance all matter. A skill may be excellent for one model and workflow and harmful for another. Evidence of quality must therefore travel with its scope, comparator, uncertainty, and expiration conditions.

This definition is the project's **reasoned synthesis**, not an existing standard or an empirically validated scoring rule.

## Reading guide and epistemic labels

- **Source observation:** a statement directly supported by a cited implementation or paper.
- **Synthesis:** an argument developed here from those observations and explicit assumptions.
- **Proposal:** an evaluation or engineering decision recommended for later testing.
- **Measured result:** reserved for an actual experiment. This project has none yet; results attributed to papers remain those authors' reported results.

The [source register](research/source-register.md) records authority, evidence strength, scope, and limitations. The [implementation audit](research/implementation-audit.md) provides exact code anchors. The [methodology](research/methodology.md) records the search and remaining uncertainties. These documents support the argument; they do not constitute independent replication.

## 1. What is the object being judged?

### 1.1 A package is not a capability

The Agent Skills specification defines a portable package centered on `SKILL.md`, with metadata, instructions, and optional resources. It specifies a representation and loading conventions, not a proof of usefulness. Runtime support can differ. [S1](research/source-register.md#s1-agent-skills-specification)

For evaluation, distinguish:

1. **The artifact:** descriptions, instructions, references, scripts, assets, and dependency declarations.
2. **The selection mechanism:** how the agent discovers and chooses it among alternatives.
3. **The intervention:** what changes when the skill is available, loaded, and used.
4. **The resulting behavior:** tool actions, output artifacts, interaction, failures, and cost.
5. **The evidence:** why observed outcomes support a claim about future use.

A document can be internally coherent but ineffective. An effective intervention can be awkwardly written. A useful package can be installed incorrectly. A good evaluator must identify which proposition is being tested rather than call all four problems “skill quality.”

The unit of judgment is consequently not `quality(skill)` in isolation. It is closer to:

> quality(skill version, agent/model version, harness, available tools and permissions, task population, user goals, operating budget, time horizon)

The qualifiers are not excuses for weak evaluation. They are the conditions under which the claim has a determinate meaning.

### 1.2 “Good” contains both factual and value judgments

Whether a workflow preserved all source records is an empirical question. Whether a five-second saving is worth a small increase in error risk is a value judgment. Whether an action was authorized is a constraint on the task. These should not be collapsed into a single unexplained score.

Three questions must remain distinct:

- **Does it work?** Does the agent achieve the intended outcome?
- **Does it help?** Is the outcome better than a fair alternative?
- **Should it be used?** Are the benefits worth the costs, risks, and ongoing obligations for this use?

A skill can answer the first question positively while failing the other two. Conversely, a skill that keeps output quality unchanged but substantially reduces review effort may be valuable. Quality is not synonymous with accuracy uplift alone.

### 1.3 The relevant alternative may be simpler

Possible alternatives include no skill, a short ordinary instruction, a maintained reference document, a deterministic tool, an existing skill, or a different operating procedure. The right comparator is what a competent user could reasonably deploy, not an artificially weak baseline.

For a one-off deterministic transformation, a script with a stable interface might be preferable to a large instructional package. A skill earns its place when reusable selection and procedural guidance add enough value to justify another maintained component. Declining to create a skill can therefore be a successful outcome of a skill creator.

## 2. Construct validity: are we measuring the thing we mean?

Measurement work distinguishes an intended construct from its operational indicators and asks whether the assumptions connecting them are defensible. Jacobs and Wallach provide a useful framework for exposing such gaps; it is a conceptual transfer to this project, not a study of agent skills. [M1](research/source-register.md#m1-measurement-and-fairness)

**Synthesis:** “skill quality” is best treated initially as a set of decision-relevant properties, not presumed to be one latent trait that every checklist item measures. There is no demonstrated reason why a longer description, more examples, and more safety prose should all increase one underlying quantity. A weighted average can conceal the failure that matters most.

### 2.1 A quality model with observable referents

| Property | What would count as evidence? | Tempting but inadequate proxy |
|---|---|---|
| Goal fidelity | Correct artifacts and state transitions satisfying the actual request | Having all expected headings |
| Marginal usefulness | Paired improvement against a relevant comparator | High with-skill pass rate alone |
| Selectivity | Appropriate invocation and abstention in a realistic skill library | Matching a few obvious keywords |
| Reliability | Repeatable authorized success, including recovery paths | One convincing demonstration |
| Robustness | Performance under declared, meaningful perturbations | Paraphrases from one template |
| Safety and scope | Correct behavior at trust, permission, and side-effect boundaries | Saying “be safe” in the instructions |
| Efficiency | Quality-cost tradeoffs including user effort and failures | Short `SKILL.md` or fewer tool calls alone |
| Maintainability | Successful updates, traceable dependencies, and regression control | Neat folder structure |
| Transferability | Evidence on the models, tools, domains, or environments claimed | A format that can be parsed elsewhere |

Confidence in these judgments is an additional dimension. **Unknown quality is not the same as poor quality.** A plausible but untested skill and a demonstrably harmful skill require different decisions.

### 2.2 Validate the evaluation instrument

For each metric, write down the inference it is supposed to support and an example that would fool it.

- A CSV “cleaning” test checks that the output has no empty cells. An agent deletes every row and passes. The metric omitted preservation and justified treatment of missingness.
- A research-report test rewards citations. The agent adds irrelevant sources. Citation count measured decoration, not evidential support.
- A safety test checks the final database. The agent makes an unauthorized change and later reverses it. The endpoint hid the prohibited action.
- A maintainability test rewards modularity. The package creates many references that the runtime never loads. File count measured decomposition, not usable organization.

**Proposal:** require both positive controls that should pass and deliberately defective artifacts that should fail. Include correct alternatives that use different wording, file ordering, or valid algorithms. An evaluator that cannot reject a known substantive defect or accept a valid alternative is not ready to establish superiority.

Test the following validity arguments rather than checking a generic “valid” box:

1. **Coverage:** are the important user goals and harms represented?
2. **Relevance:** are irrelevant factors such as prose length driving the score?
3. **Convergence:** do independent artifact checks and informed human judgments broadly agree where they should?
4. **Discrimination:** can the evaluator distinguish meaningful improvements from superficial changes?
5. **Prediction:** does the result anticipate performance on independently collected future tasks?
6. **Consequences:** what behavior will optimizing this metric encourage?

These are proposed questions for this project. They are not a claim that psychometric tests designed for people can simply be reused for software agents.

## 3. Marginal usefulness is a causal question

### 3.1 State the estimand before running the test

Let `X` denote a complete task episode: request, preceding context, input artifacts, environment state, and authorized operations. Let `D` be the intended distribution of episodes. Fix a model, harness, and budget policy. Let `Z = 1` mean the candidate skill is available under the intended invocation policy and `Z = 0` mean the comparator is used. Let `U` represent an explicitly chosen utility of the observed outcome, including costs where commensurable.

The deployment question is:

`Delta_D = E[U(Y(1, X)) - U(Y(0, X))], for X drawn from D.`

This is a proposed causal estimand, not an equation that makes unmeasured utility objective. If harms cannot defensibly be traded against benefits, evaluate them as constraints instead of assigning an invented monetary weight.

The same episode cannot usually be rerun in the same mutable world without interference. Use resettable copies, controlled simulations, or another design that makes the comparison credible. Match the task and initial state, randomize or interleave condition order where appropriate, repeat stochastic runs, and keep treatment-specific artifacts inaccessible to other runs.

### 3.2 Separate three experiments

1. **Deployment effect:** install the skill in a representative catalog and let normal selection operate. Include relevant and irrelevant requests. This captures missed activation, false activation, catalog interference, and execution.
2. **Conditional execution capability:** force use on a predeclared set of suitable tasks. This diagnoses whether the body and resources can help when available. It does not measure natural activation.
3. **Mechanism ablations:** compare the full package with relevant alternatives such as instructions only, resources only, ordinary documentation, or a concise prompt. These investigate what caused an improvement.

Do not compare only the tasks on which the agent happened to activate a skill with all no-skill tasks. Activation is selected by the system and may be correlated with difficulty. That comparison changes the population and can produce a misleading effect.

### 3.3 Fairness of the comparison depends on the claim

If a skill bundles a useful script, giving that script only to the treatment is reasonable when measuring the value of the **whole package**. It is insufficient when claiming that the **instructional method** is better. A tool-only ablation distinguishes these claims.

Likewise, comparing a creator allowed expensive iterative research with a baseline allowed one short generation tests a combined process-and-budget intervention. That may be a useful product comparison, but it is not an equal-budget comparison of writing quality.

Report both fixed-budget comparisons and achievable quality-cost tradeoffs where practical. Work on agent evaluation has shown why cost and the strength of simple baselines can change conclusions about elaborate systems. [M3](research/source-register.md#m3-ai-agents-that-matter)

### 3.4 Beware of ceiling and floor effects

A 98% baseline leaves little room for accuracy gains; a skill might still reduce cost or variance. A 0% baseline and 0% treatment may mean an impossible task, missing tool, bad grader, or ineffective skill. Neither case supports a blanket conclusion from the average alone.

Keep an absolute adequacy criterion alongside the relative effect. Improving from 10% to 20% is a large relative gain but may still be unusable. Report absolute percentage-point differences; use relative or normalized gains only with their denominators visible.

## 4. Activation is an information-retrieval problem with consequences

The description acts partly as an index into procedural information. Information science distinguishes relevance to a user's situation from mere topical resemblance. Borlund's task-centered evaluation framework is an instructive analogy, not evidence that simulated users reproduce human use of skills. [M4](research/source-register.md#m4-interactive-information-retrieval)

**Synthesis:** “contains the word PDF” is not an adequate definition of “should activate a PDF skill.” The needed operation, available tools, user constraints, stage of work, and competing skills matter.

### 4.1 Define relevance without making the label circular

Before testing, specify when the skill is appropriate and when it is unnecessary, unsupported, or subordinate to another workflow. Label realistic contexts under that policy, allowing ambiguous cases to remain ambiguous until adjudicated. Do not define “relevant” retrospectively as “the candidate happened to win.” That would guarantee favorable labels by construction.

Also recognize the limitation: agreement with a relevance policy is not proof that activation improves utility. Measure both label agreement and downstream effects. A base model may solve an easy request without loading a skill; whether that is an error depends on the actual operating contract.

For binary labels, report:

- Precision = appropriate activations / all activations
- Recall = appropriate activations / all cases where activation is expected
- False-positive rate = inappropriate activations / all cases where activation is not expected
- False-negative rate = missed expected activations / all cases where activation is expected

Report counts and uncertainty. Undefined ratios, such as precision with no activations, should be marked undefined rather than silently presented as perfection.

### 4.2 The base rate changes the meaning of a score

**Illustrative calculation:** if only 1% of requests are relevant, recall is 90%, and false-positive rate is 5%, expected precision is:

`(0.01 * 0.90) / ((0.01 * 0.90) + (0.99 * 0.05)) = 15.4%.`

A balanced trigger test can look encouraging while the deployed agent invokes the skill mostly unnecessarily. Balance development sets if useful for diagnosing errors, then weight or resample to a defensible deployment mixture. If prevalence is unknown, show sensitivity to plausible mixtures instead of inventing one.

Use hard negatives from adjacent work, paraphrases, implicit requests, multi-turn context, and catalog competition. A positive-only trigger set cannot estimate precision. An explicit “use this skill” test cannot estimate autonomous discovery.

### 4.3 Selection is not the end of the pipeline

Record whether the skill was discoverable, selected, read, understood sufficiently to act, and used to produce a verified outcome. These are diagnostic events, not independent probabilities to multiply casually. Skill usage can be high while task quality is low.

The selected policy should minimize the costs of missing useful guidance and imposing irrelevant guidance, subject to safety constraints. There is no universally correct precision-recall balance, and making descriptions more insistent is not inherently an improvement.

## 5. Generalization requires a declared task population

“General-purpose” is a scope claim. It requires evidence at the corresponding level of novelty, not a larger collection of near-duplicate prompts.

Distinguish generalization across:

- **Instances:** new files, users, values, or requests from the same procedure
- **Surface forms:** paraphrases, languages, formatting, and order of presentation
- **Procedures:** new combinations, exceptions, or task templates
- **Domains:** materially different bodies of knowledge and success criteria
- **Environments:** tool versions, operating systems, permission profiles, and network availability
- **Agents:** models, context limits, harnesses, and selection policies
- **Time:** changed APIs, sources, dependencies, and user practice

A creator tested on five variants of spreadsheet cleanup has not been evaluated as a general creator. Splitting examples at random may leave both sides sharing the same template, repository, or oracle. Split at the level corresponding to the claim. Preserve grouping in the analysis as well as in data preparation.

**Proposal:** construct a task matrix before authoring the candidate. Include common cases, costly edge cases, plausible off-task requests, and unsupported conditions. Record why each stratum belongs. Do not quietly remove difficult scenarios because they are inconvenient to verify.

Two complementary samples are useful:

1. A prevalence-oriented sample for expected deployment usefulness
2. A deliberately difficult or risk-oriented sample for boundary discovery

They answer different questions. Report them separately; do not mix adversarial cases into a prevalence estimate without justified weights.

## 6. Reliability, robustness, and safety are different

### 6.1 Reliability is repeatable acceptable performance

Repeated runs reveal variation that a single demonstration cannot. The original tau-bench distinguishes the chance that all `k` trials succeed, `pass^k`, from the chance that at least one succeeds, `pass@k`. Its own reward discussion also acknowledges that a correct final state can miss a policy violation. [E1](research/source-register.md#e1-tau-bench)

**Proposal:** define a successful episode to require the desired result **and** compliance with important authorization and process constraints. Track repeated success per task, not merely the best attempt. An agent that succeeds once after many retries is a different product from one that succeeds consistently on the first authorized attempt.

For a task with independent, identically distributed trial success probability `p`, all-`k` success is `p^k`. Across heterogeneous tasks, average the task-level quantities; the `k`th power of the pooled mean is generally different. Real retry episodes may be dependent because they retain state or receive feedback. Measure that actual retry policy separately rather than applying an independence formula to it.

### 6.2 Robustness needs a perturbation model

Test meaningful changes, not arbitrary noise:

- A malformed input with a recoverable defect
- A reference that is unavailable or out of date
- A tool timeout after a possibly successful mutation
- A missing permission or authentication requirement
- An ambiguous request whose answer changes the correct action
- Extra irrelevant documents or conflicting lower-trust text
- A long conversation that threatens context retention
- A supported tool-version change

Specify which changes should preserve the answer and which should change it. Reordered data might preserve an aggregate; a changed date range should change it. A metamorphic test is useful only if its expected relation is justified.

Robustness includes an appropriate stop, clarification, or handoff when completion is unsafe or impossible. Penalizing every non-completion as incompetence would teach the creator to suppress necessary boundaries.

### 6.3 Safety is behavior at boundaries, not a prose property

Review the package for unnecessary privileges, hidden network access, destructive defaults, bundled executables, dependency provenance, and insecure handling of data. Then test behavior when an untrusted document tries to change the task or when a tool returns misleading instructions. AgentDojo is primary evidence that utility and attack resistance should be tested together in stateful tool environments. It does not certify a skill's safety. [E2](research/source-register.md#e2-agentdojo)

Important proposed invariants include:

- Task data cannot authorize a new action.
- Installing or invoking a skill does not confer permissions the user did not grant.
- A retry of an uncertain mutation must not create an unobserved duplicate.
- Failure reporting must not falsely claim completion.
- Temporary artifacts, logs, and outputs must obey the intended data boundary.

Where possible, enforce critical restrictions in tools, sandboxes, schemas, and permission checks. Natural-language instructions are useful guidance but are not a substitute for enforcement.

### 6.4 Zero observed failures is not a guarantee

**Illustrative calculation:** under independent identically distributed Bernoulli trials, with zero observed failures in `n` trials, a one-sided 95% upper confidence bound on failure probability is `1 - 0.05^(1/n)`. It is about 13.9% for 20 trials, 3.0% for 100, and 1.0% for 300.

Those assumptions fail if the scenarios are near-duplicates or omit entire failure classes. The calculation therefore cannot certify safety; it demonstrates why “passed our small suite” is much weaker than “rarely fails.” Severity-based review and adversarial testing remain necessary, and neither establishes an absolute guarantee.

## 7. Efficiency and maintainability belong in the judgment

### 7.1 Measure cost at the boundary the user pays for

Record model tokens by category where available, tool charges, elapsed time, retries, user interruptions, review effort, and failure recovery. Distinguish warm and cold caches if they materially change the result. A shorter instruction file can produce a longer, more confused execution.

Do not optimize raw tool-call count in isolation. One extra verification call may prevent expensive rework. Conversely, ritual checking may consume time without changing a decision. Judge a step by the information or risk reduction it contributes.

Creation and maintenance costs are amortized over expected uses:

`lifecycle cost = creation + validation + updates + sum of execution and recovery costs.`

This is an accounting proposal. Estimate uncertain terms as ranges. A highly specialized skill used once may not repay a lengthy creation process; one used frequently may justify substantial up-front testing.

### 7.2 Information architecture should make decisions easier

**Synthesis:** the useful amount of instruction is the amount that changes the agent's relevant decisions. Concision, examples, scripts, and progressive disclosure are design hypotheses about achieving that goal, not intrinsic merits or universal thresholds.

For each substantial component ask:

- Which error, uncertainty, or repeated effort does it address?
- Is that problem actually observed or credibly required by the task?
- Will the agent find this information at the moment it matters?
- Does it conflict with another instruction or with current tool behavior?
- Could a simpler representation provide the same benefit?
- What would falsify our belief that it helps?

Use ablations when the answer matters. Remove a suspected redundant section and retest. Replace variable prose with a deterministic helper where the operation is stable. Keep flexible judgment where valid solutions differ. A rule learned from one failure should not silently become a universal requirement.

### 7.3 A skill is a maintained dependency

Record its intended environment, dependency versions or supported ranges, sources of changeable claims, owner, regression tests, and conditions for re-evaluation. Test an actual small update: can a maintainer find the affected rule, change it without contradictory copies, and determine whether behavior regressed?

Evaluate composition. Two individually helpful skills may disagree about tool choice, output format, or verification. A growing catalog also changes selection costs and collision rates. The library is part of the environment, not a neutral container.

A model upgrade can eliminate the knowledge gap that justified a skill. The correct response may be retirement or simplification rather than indefinite accumulation of instructions.

## 8. What the present evidence does and does not establish

### 8.1 Public creators are strong baselines, not scientific verdicts

The inspected OpenAI creator emphasizes reusable resources, focused instructions, validation, and iteration. The inspected Anthropic creator adds a substantial development loop with baseline runs, graders, human review, and trigger optimization. These are valuable implementation choices. Neither source alone demonstrates that its authoring method is superior across task distributions. Exact versions and concrete limitations are in the [implementation audit](research/implementation-audit.md).

A particularly important distinction: Anthropic's description optimizer withholds test results from the improvement model, but selects the best iteration using that split. This is a useful **selection** procedure; its selected score is not an untouched final generalization estimate. A separate final evaluation is needed for that claim. This is a methodological distinction, not an allegation of misconduct. [S3](research/source-register.md#s3-anthropic-skill-creator), [M2](research/source-register.md#m2-model-selection-bias)

### 8.2 Direct skill experiments are relevant but provisional

Three primary 2026 preprints deserve attention because they actually compare skill conditions. They have not been independently reproduced here. Their populations and interventions differ:

- **SkillsBench** reports a 16.2 percentage-point average gain from curated skills across 84 evaluated tasks and seven agent-model configurations, with negative effects on some tasks. Its task-stratified length and module-count findings are associations, not randomized proof of an optimal package size. [D1](research/source-register.md#d1-skillsbench)
- **SWE-Skills-Bench** reports about a 1.2-point improvement across 565 task instances using one solver configuration, with a no-skill pass rate near 90%. Its methods contain inconsistent descriptions of skill placement that need repository-level reconciliation before reuse. [D2](research/source-register.md#d2-swe-skills-bench)
- **SkillLearnBench** explicitly selects skill-dependent tasks and tests generated skills with a fixed solver. Its adapted single-round “Skill Creator” baseline is not equivalent to the full current Anthropic iterative workflow. [D3](research/source-register.md#d3-skilllearnbench)

**Synthesis:** these findings do not support “skills always help,” “skills are useless,” or “models cannot create useful skills.” They motivate testing the interaction among content, baseline competence, task selection, and runtime. Their headline averages should not be pooled into a universal expected gain. A benchmark designed to expose a procedural gap and one with a high-performing baseline estimate different things.

### 8.3 Important disagreements should become tests

Public guidance often favors shorter instructions and encourages activation. Both can be reasonable development heuristics. The empirical questions are whether removing text loses critical information and whether extra activation improves outcomes in the actual catalog.

Similarly, repeatable grading is not necessarily valid grading; more tests are not necessarily broader tests; and a fresh conversation is not necessarily an isolated environment. These distinctions should shape the future creator rather than becoming slogans in its prompt.

## 9. A defensible evaluation protocol

The following is a **proposal for later experimental design**, not an already executed benchmark.

### Stage A: Write the evaluation contract

Before seeing candidate outputs, declare:

1. User goals, intended use, excluded uses, and important harms
2. Task population, sampling rationale, strata, and weighting
3. Model, harness, tools, permissions, catalog, context, and budget policies
4. Comparator and what causal question each ablation answers
5. Primary outcomes, mandatory invariants, graders, and adjudication process
6. Minimum worthwhile improvement and unacceptable regressions
7. Planned repetitions, uncertainty method, missing-data rules, and stopping rule
8. Which cases are for development, selection, and final confirmation

This is where a domain expert's judgment is especially valuable. More statistical sophistication cannot repair an evaluation of the wrong task.

### Stage B: Validate the harness and evaluator

Check that the treatment actually changes skill availability and that the baseline cannot retrieve it indirectly. Test known-good and known-bad artifacts. Confirm state reset, trace capture, permissions, tool versions, and timeout behavior.

Use deterministic checks for mechanically decidable properties. Use calibrated human review where the desired quality is contextual or subjective. LLM judges can scale review but require calibration; known position and verbosity effects make unvalidated judge scores insufficient. [E3](research/source-register.md#e3-llm-as-a-judge)

Blind provenance where feasible, randomize output order, include order-swapped checks, preserve ties and uncertainty, and adjudicate consequential disagreements. Do not assume a different model family automatically creates independent errors. Treat artifacts being graded as untrusted inputs to the evaluator as well.

### Stage C: Run paired and isolated trials

Run the same sampled episodes under each condition with clean context and independent mutable state. Keep model and permission settings fixed. Interleave runs when service drift or load could matter. Log all attempts, including failures and censored runs.

Classify infrastructure errors separately from task failures. Do not silently count a crashed trigger test as a correct abstention or discard inconvenient timeouts. Predeclare when a technical rerun is allowed, preserve both records, and report results with enough detail to show the impact of exclusions.

### Stage D: Estimate effects, not just scores

Report paired outcome differences, per-task results, important strata, severe failures, costs, and uncertainty. Keep the unit of analysis honest: twenty variants of one template are not twenty independent task families. Repeated seeds reduce uncertainty about that task's behavior; they do not create new domain coverage.

Choose an uncertainty method suitable for the design. A task- or family-clustered bootstrap may suit a sufficiently broad sampled collection; exact paired methods or a justified hierarchical model may suit other designs. Very few clusters can make any population interval unstable. State assumptions and avoid substituting a standard deviation for a confidence interval on the effect.

Determine sample size from the decision, effect scale, risk tolerance, variation, and cost. A few pilot cases can find large defects; they cannot establish small differences or rare-event safety. Freeze confirmatory endpoints and handle multiple comparisons explicitly. If optional stopping is needed, use a valid sequential design rather than repeatedly checking until a favorable result appears.

### Stage E: Protect generalization claims

Keep development and selection feedback separate from the final evaluation. Once a final test is used to choose a version, threshold, rubric, or stopping point, it has become development evidence for that decision. Cawley and Talbot establish the general risk of selection bias from optimizing finite-sample criteria. [M2](research/source-register.md#m2-model-selection-bias)

Also distinguish:

- **Model pretraining contamination:** public tasks or answers may already have been learned.
- **Creator contamination:** the author sees held-out tasks, solutions, or grader details.
- **Execution contamination:** trials share files, traces, memory, caches with semantic content, or answers.
- **Evaluator contamination:** graders know which candidate is intended to win or adapt the rubric after seeing its outputs.

Use provenance records, deduplication, grouped splits, and independently authored cases. Keep final cases outside the candidate's accessible workspace. Publishing them in this public repository before evaluation would remove that protection. A separate authorized custodian or environment is needed; no such holdout exists yet.

Contamination detection is not a universal certificate of cleanliness. Oren and colleagues' test, for example, has specific access and exchangeability assumptions and targets particular forms of contamination. Failure to detect leakage cannot establish its absence. [E4](research/source-register.md#e4-test-set-contamination)

### Stage F: Make a bounded decision

A proposed decision rule is:

- Block release for unresolved severe violations or an invalid evaluation.
- Require adequate absolute performance on critical uses.
- Require evidence of worthwhile benefit over the comparator, or a justified quality-cost tradeoff, under the declared population.
- Require uncertainty and coverage to be acceptable for the intended risk.
- Report subgroups where the skill harms performance or remains untested.
- Schedule re-evaluation when the model, runtime, dependencies, or usage distribution changes materially.

These are proposed gates. Neither “95% confidence” nor a particular pass rate is a universal release standard. Risk tolerance and minimum effects must be set before the confirmatory result, with reasons.

## 10. Worked example: a data-cleaning skill

This hypothetical example shows how the framework changes the work.

**Claim:** a skill helps an agent prepare customer CSV files for analysis while preserving source data and respecting instructions about missing values.

**Population:** recurring operations on several supported CSV schemas, with an explicitly declared mix of common requests and exceptions. It does not include arbitrary medical datasets or undocumented database mutations.

**Comparators:** the same agent with ordinary tools and no skill; a short task instruction; the same helper script without the full package if mechanism matters.

**Activation cases:** cleaning a file should normally activate it; explaining what CSV means should not. “Make the table tidy” needs context. A request to delete records must be distinguished from one to report missingness.

**Outcome checks:** correct row-level transformations against a validated oracle, schema preservation, accurate summaries, readable output, and no unauthorized source overwrite. Test empty files, duplicated identifiers, missing columns, encoding problems, and tools that fail after writing.

**Generalization:** group by data source and transformation family. Keep independently prepared schemas or combinations for confirmation. Merely replacing names and dates does not demonstrate general-purpose data cleaning.

**Efficiency:** include review and correction effort. A more verbose summary may save user effort; a shorter agent run that drops ambiguous records may create expensive rework.

**Decision:** deploy only for the verified use envelope. If the ordinary script performs as well with less complexity, retain the script and simplify or retire the skill.

No number in this example is a proposed pass-rate threshold, and no result has been measured.

## 11. What would make a skill-creation skill superior?

A creator is evaluated through a nested process:

`creation request -> creator + permitted evidence -> generated skill -> independent solver on new tasks -> judged outcomes and lifecycle cost.`

There are therefore two important distributions: **requests to create skills** and **future tasks those skills must support**. Optimizing only the appearance of generated `SKILL.md` files misses the second. Testing only a handpicked excellent output misses the first.

**Proposal:** compare the candidate with pinned OpenAI and Anthropic creators and a strong concise-prompt baseline. Give each fair access to the same task requirements, domain references, tools, and feedback under declared budgets. Preserve the native runtime comparison and any adapted cross-runtime comparison as separate experiments. An adaptation may materially change the baseline.

Repeat creation when feasible because a creator can produce variable artifacts. Evaluate those artifacts with fixed downstream solvers and withheld downstream tasks. Hold out entire creation families for the broader generality claim. Include cases where a tool, reference, or no new skill is the appropriate solution. Charge the creator for research, clarification, debugging, and evaluation effort rather than hiding these costs.

Success would be a statement such as:

> Under these pinned creators, budgets, environments, and sampled creation-task families, the candidate produced skills with a specified improvement in independently evaluated downstream utility, with stated uncertainty and no unacceptable regression on the tested constraints.

It would not establish superiority to every present or future creator. The research ambition should be strong enough to win a fair test and disciplined enough to report a loss.

## 12. Conclusions and unresolved questions

The central claim is simple: **evaluate the change a skill causes, for the users and conditions that matter**. Everything else follows from taking that sentence seriously.

1. Artifact inspection supplies hypotheses and catches defects; it cannot establish marginal usefulness.
2. Selection and execution need separate diagnostics and a combined deployment test.
3. The task distribution, comparator, constraints, and measurement validity determine what a score means.
4. Reliability and safety require traces, repeated trials, adverse conditions, and explicit uncertainty.
5. Concision, modularity, and detailed procedure are contingent design choices.
6. A creator's quality is ultimately about the skills it produces under fair resource and information constraints.

Before implementation, the project still needs independent criticism of this construct and decision model; a better justified target distribution; a risk-proportionate statistical design; a practical holdout boundary; calibrated graders; and a faithful baseline execution plan. The highest-priority next action is the fresh-context critique in [TASKS.md](TASKS.md), not writing the final meta-skill.
