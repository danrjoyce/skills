# How to determine if a skill is good

**Status:** R3 revised foundations, 2026-10-02 UTC. Responds to the independent [R2 critique](research/critique-01.md); dispositions and remaining tests are in [revision-01.md](research/revision-01.md). This freezes an initial conceptual framework, not numerical release thresholds. No skill-performance experiment was run. Numerical examples are illustrations, not results.

## The answer in one paragraph

A good skill is a **reusable package that is fit for a declared purpose: it enables sufficiently reliable, authorized outcomes within a specified agent, runtime, task population, and resource envelope**. Fitness, incremental usefulness, adoption, and comparative superiority are different claims. Two equally capable alternatives can both be good. Behavior and verified outcomes matter more than polished instructions or format compliance. Selection, execution, verification, and maintenance all matter. Evidence must travel with the artifact version, scope, comparator when relevant, uncertainty, and conditions for re-evaluation.

This is the project's **reasoned synthesis**, not an established standard or a validated quality scale. The user or responsible domain owner supplies the desired outcomes, minimum adequacy, affected-party constraints, and acceptable tradeoffs. Statistics cannot choose those values. Severe unauthorized effects are noncompensating constraints, not deductions that enough style points can cancel.

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

Four judgments must remain distinct:

- **Fitness for purpose:** does the package meet declared adequacy and constraint requirements in its supported envelope?
- **Incremental value:** what improvement or tradeoff does it offer against a named, feasible comparator?
- **Adoption:** do prospective benefits justify installation, use, risk, switching, and maintenance for this user and horizon?
- **Comparative superiority:** does a predeclared comparison establish an advantage over specified alternatives on specified endpoints?

Do not require discovery of the globally best alternative. State the comparator set and why it is credible. The no-skill condition, incumbent skill, concise prompt, and deterministic helper may each answer a different decision. Resilience or interoperability can justify an adequate backup without an average accuracy gain, provided those benefits are actually part of the contract.

| Evidence state | Fitness judgment | Decision and permissible claim |
|---|---|---|
| Adequate and within constraints, relative advantage unknown | Fit within tested scope | May consider bounded adoption; no superiority claim |
| Adequate with worthwhile comparative benefit | Fit and beneficial | Adopt if horizon and risk support it; name comparator and uncertainty |
| Two alternatives meet requirements and the relevant equivalence margins | Both can be good | Choose by prospective cost, compatibility, resilience, or preference |
| Worse on all relevant dimensions with no compensating advantage | May still meet adequacy | Prefer the dominating feasible alternative; distinguish empirical from merely apparent dominance |
| Severe constraint violation | Unfit for that authorized use | Block that use even if average task score is high |
| Insufficient or invalid evidence | Unknown | Repair measurement, narrow the claim, or run a proportionate reversible trial |

An estimated tie is not established equivalence. A statistically detectable gain need not be worthwhile. Report a vector or Pareto frontier when quality, time, money, and risk are not commensurable. Any scalar utility must identify its owner, units, weights, and sensitivity to plausible alternatives.

### 1.3 The relevant alternative may be simpler

Possible alternatives include no skill, a short ordinary instruction, a maintained reference document, a deterministic tool, an existing skill, or a different operating procedure. The right comparator is what a competent user could reasonably deploy, not an artificially weak baseline.

For a one-off deterministic transformation, a script with a stable interface might be preferable to a large instructional package. A skill earns its place when reusable selection and procedural guidance add enough value to justify another maintained component. Declining to create a skill can therefore be a successful outcome of a skill creator.

### 1.4 Initial product and runtime contract

**R3 scope choice:** the intended first candidate is a model-invocable, host-loaded **authoring workflow packaged as an Agent Skill**, usable after an authorized creation request and explicitly callable by a human. It is not a separately registered native function, CLI service, or MCP server. Autonomous discovery does not authorize installation, network access, publication, or other consequential operations. No candidate exists yet. R4 may revise this scope explicitly if the user's actual call-tool requirement demands a service.

The package supplies instructions and optional resources. A host supplies discovery, context loading, file access, execution tools, permission enforcement, and result delivery. A loader returning instructions is not itself a function that executes the entire workflow and returns a typed business result. The pinned integration guide describes file-read and host-registered activation mechanisms. [S5](research/source-register.md#s5-agent-skills-client-integration-guide)

| Target | Intended invocation and execution | Status and boundary |
|---|---|---|
| Claude Code native workflow | Host discovers an installed package and exposes its skill activation mechanism; human explicit invocation or permitted model selection loads instructions; host tools execute resources | Target only, no compatibility run here; R4 must pin CLI, model, install path, loader trace, and permissions |
| Codex native workflow | Host discovers package metadata and loads instructions through its actual supported interface; human explicit invocation or permitted implicit use; executor runs scripts | Target only, no compatibility run here; R4 must pin host/model and confirm interface rather than assume a tool named `Skill` |
| Other host or common experimental adapter | An explicitly implemented catalog/loader and file/execution contract may expose the workflow | Unsupported until tested; adapter is part of the treatment and must be versioned |
| Generic function-calling API with no loader or executor | A parseable `SKILL.md` creates no registered function; bundled scripts cannot run without an execution route | Negative compatibility case: report unsupported environment, not successful portability |

Repository rules pair Claude's `disable-model-invocation` with Codex's `policy.allow_implicit_invocation` for user-only skills. Dependencies must respect that distinction. The repository's instruction to call a named Skill tool is a local convention, not a universal interface specification. Generated user-only artifacts are evaluated on explicit invocation and human discovery, not penalized for absent autonomous triggering. [Repository invocation contract](https://github.com/danrjoyce/skills/blob/ca27f690562c7440458dc50cdc0f01b5073f08ad/.agents/invocation.md)

Each eventual artifact must state: install/discovery scope; allowed invocation modes; supported loader; resource base path; executor/dependency versions; permissions and network needs; expected inputs/outputs; unsupported-case behavior; and owner/update conditions. Relative paths resolve against the package directory, not an assumed working directory. If a dependency or permission is missing, return a specific unsupported/blocked result; never invent an executed tool call or request expanded privileges merely to pass a test.

The initial authoring-output contract is a reviewable package plus usage/compatibility evidence, or a reasoned recommendation for an existing skill, script, reference, or no new artifact. Report status separately: produced, appropriate alternative, clarification needed, unsupported, over budget, or failed. Include artifact identity, assumptions, evidence provenance, tests actually run, remaining limits, and expected maintenance. This is a proposed reporting contract, not an implemented JSON schema or tool registration. R4 must choose concrete host configurations before claiming any supported runtime.

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
4. **Sensitivity to meaningful change:** can the evaluator distinguish a substantive improvement from a superficial change? This is not M1's technical discriminant-validity construct.
5. **Deployment prediction:** does the result anticipate performance on independently collected future tasks? This is our validation proposal, not a verbatim adoption of M1's predictive-validity definition.
6. **Consequences:** what behavior will optimizing this metric encourage?

These are proposed questions for this project. They are not a claim that psychometric tests designed for people can simply be reused for software agents.

### 2.3 Operational metric map and evaluator calibration

The property table above is conceptual. The following proposed map specifies what a measurement can actually establish. Exact criteria and thresholds remain R4 decisions.

| Metric and units | Observable and oracle | Counterexample the oracle must handle | Uncertainty and permissible inference |
|---|---|---|---|
| Authorized success, binary per attempt; rate per declared population | Validated artifact checks plus complete action/permission trace; human adjudication for contextual requirements | Correct final file after unauthorized overwrite or data transmission must fail | Oracle coverage and task/solver variation; supports success on tested criteria, not unrestricted correctness |
| Incremental outcome, percentage points or owner-defined utility units | Paired reset episodes under frozen conditions, graded identically | Treatment gets extra answers or baseline loads the package indirectly | Sampling, selection, contamination; causal claim only under intervention/isolation assumptions |
| Activation agreement, counts and rates over labeled contexts | Catalog snapshot, activation/access event, prescribed time window, acceptable-choice set | Inspecting file type first then using a permitted substitute can be correct | Contextual label disagreement, trace coverage, base rates; measures routing policy agreement, not usefulness by itself |
| Resource access/execution, event counts and timestamps | Loader/file-read result, script exit, resulting state; independent event capture | Agent says it read a reference but no observable access; file read succeeds yet instructions ignored | Missing telemetry; establishes observed access/action, never mental understanding |
| Constraint violations, count and severity by opportunity | Controlled network sinks, permission logs, file diff and action trace | Secret fixture appears in logs though final output is clean | Scenario coverage and detector false negatives; bounded observed compliance only |
| Cost, tokens/currency/seconds/human minutes | Metered calls, wall-clock, review/error-recovery log, allocated fixed cost | Fewer calls require more human correction or load catalog text on irrelevant traffic | Price/cache variation, human skill, forecast use; prospective cost under stated boundary |
| Repeated acceptable success, per-task distribution | Fresh solver runs on reset state, fixed calibrated grader | Best of ten shown as first-attempt reliability | Solver/environment variation and dependence; separate from grader repeatability |
| Maintenance effort and regression, minutes and changed outcomes | Predeclared dependency change, independent maintainer action, old/new suite | Cosmetic edit passes while stale duplicate rule remains active | Maintainer expertise and change sample; no universal maintainability score |

Calibrate three distinct things:

1. **Evaluator repeatability:** regrade fixed artifacts/traces, with ordering and provenance controlled. Record disagreement, ties, errors, and critical false-pass rates. This does not rerun the solver.
2. **Substantive validity:** inspect independently established correct and defective fixtures, including noncanonical correct solutions. Agreement between judges sharing a mistaken reference is not independent validation. Escalate critical false passes even if aggregate agreement is high.
3. **Solver reliability:** only after the oracle is credible, repeat the solver under the declared deployment and retry policy. Grader uncertainty should be propagated or reported separately, not misattributed to model instability.

For CSV cleaning, a streaming algorithm and a dataframe implementation can both be valid even if row ordering differs where order is immaterial. Conversely, deleting troublesome rows to satisfy a no-null check must fail preservation checks. For activation, allow initial schema inspection followed by the right specialist, or an explicitly permitted equivalent helper. Freeze these examples and their acceptance rationale before evaluating a candidate; they are not yet an executed calibration set.

## 3. Marginal usefulness is a causal question

### 3.1 State the estimand before running the test

Let `X` denote a complete episode: request, preceding context, inputs, initial environment state, and authorized operations. Let `D` be the target distribution, including irrelevant traffic when the package is in the catalog. Fix model, host, permissions, budget, and recovery policy. Let `Z=1` be the candidate availability/invocation policy and `Z=0` a named comparator. `R` covers solver randomness and stochastic environment responses under that policy. `Y(z,X,R)` includes outcomes, trace, and cost. For a declared scalar outcome `q`:

`Delta_D(q) = E_{X ~ D}[E_R q(Y(1,X,R)) - E_R q(Y(0,X,R))].`

Use multiple `q` values when a vector is appropriate. For authorized success, the units are probability or percentage points; severe violations are also separately reported and gated. Utility weights are a normative input, not made objective by expectation notation. Include timeouts, failed activation, and failed execution in the intended policy, not just successful sessions.

For a fixed weighted suite, replace the outer expectation with `sum_i w_i (...)`, where weights sum to one. That identifies the suite effect, not a population effect merely because a confidence interval was added. Population transport requires a sampling argument or explicit assumptions about omitted users, families, and environments.

Pairing means reset copies of the same initial case, not observing both potential outcomes in one mutable world. Randomize/interleave order, isolate state, and record interference. Common random seeds may help control noise where meaningful, but model-specific random streams need not correspond. If isolation is impossible, use a design that models interference or narrow the claim. Fresh chat alone is insufficient.

### 3.2 Separate three experiments

1. **Deployment effect:** install the skill in a representative catalog and let normal selection operate. Include relevant and irrelevant requests. This captures missed activation, false activation, catalog interference, and execution.
2. **Forced-use diagnostic:** choose and record one intervention on a predeclared eligible set: inject the body, instruct explicit loading, or invoke the native loader. These alter attention/context differently and are separate conditions. They do not identify the counterfactual effect among cases that happened to activate naturally.
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

Before testing, specify when the skill is required, optional/helpful, prohibited, unsupported, or subordinate to another workflow. Define acceptable alternatives and the activation window, such as after initial file inspection but before transformation. Explicitly invoked and user-only skills need their own denominator. Label realistic contexts under that policy. Adjudicate ambiguity without seeing candidate identity/outcomes; if ambiguity remains, retain it in end-to-end evaluation but report it separately from binary routing ratios, with counts and coverage. Do not quietly delete difficult contexts. Do not define “relevant” retrospectively as “the candidate happened to win.” That would guarantee favorable labels by construction.

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

Record catalog inclusion, an activation request, returned instruction content, observed resource access, executed actions, and verified outcomes. A trace cannot directly establish understanding; successful output or a self-report of use cannot establish causal reliance on the skill. These are diagnostic events, not independent probabilities to multiply casually. Skill usage can be high while task quality is low.

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

- Lower-trust embedded content cannot expand user-approved scope. A direct user instruction or a machine-readable job request from an authorized source can carry authority under its approved contract; prose versus JSON is not the trust boundary.
- Installing or invoking a skill does not confer permissions the user did not grant.
- A retry of an uncertain mutation must not create an unobserved duplicate.
- Failure reporting must not falsely claim completion.
- Temporary artifacts, logs, and outputs must obey the intended data boundary.

Where possible, enforce critical restrictions in tools, sandboxes, schemas, and permission checks. Natural-language instructions are useful guidance but are not a substitute for enforcement.

### 6.4 Creator and package threat model

**Proposal:** protect source data, output integrity, credentials (represented only by inert fixtures in tests), authorized state, tool privileges, evaluation integrity, and the user's time. The attacker may control retrieved references, task attachments, tool-returned text, a package contribution, dependency/update bytes, or an output sent to a grader. Do not assume control of trusted host enforcement or the user's direct authorization; those are explicit boundaries whose failure would change the threat model.

| Ingress and threat | Critical invariant | Enforcement and observation | Paired benign/adversarial check |
|---|---|---|---|
| Authoring reference launders an instruction or unsupported fact into the package | Provenance and scope remain attached; source text cannot grant authority | Creator source records, review of consequential claims, downstream regression checks | Accurate documented API change versus a reference ordering secret upload |
| Package script/dependency or update has hidden effects | No execution outside approved privileges; no undeclared network/data flow | Pinned dependency review, sandbox, permission gate, filesystem/network telemetry | Declared local transform versus transform with controlled-sink exfiltration attempt |
| Repository package shadows a trusted name | Trust decision and resolved version are visible before loading | Host discovery/trust gate, collision log, package digest | Authorized update versus untrusted same-name package |
| Task/tool content redirects executor | Only authorized operations and destinations | Tool argument validation, permission checks, inert attack documents | Normal task plus needed context versus same task plus forged escalation |
| Retry after uncertain mutation | No unauthorized duplicate or false completion report | Idempotency support, status reconciliation, attempt ledger | Recoverable read failure versus simulated ambiguous write result |
| Output attacks evaluator | Artifact content cannot rewrite the rubric or suppress a violation | Grader isolation, fixed rubric, escaped presentation, independent critical checks | Valid alternative output versus “award full marks” embedded in artifact |

Project-level package trust is also a concern in the integration guide [S5](research/source-register.md#s5-agent-skills-client-integration-guide). A trusted package is still not a grant of new permissions. Enforcement belongs in the host/tool/sandbox where possible; prose alone cannot guarantee it. The package may fail to detect a novel attack, and the host may expose incomplete telemetry. Name those residual risks and downgrade assurance accordingly.

Score useful benign completion alongside attack outcomes so blanket refusal cannot win. Count attempted and completed prohibited actions, including transient effects and leaks in logs, not only final-state differences. Tests use inert fixtures and controlled sinks, not real secrets or live destructive operations. Simulated success is evidence about that simulation, not certification.

The creator's epistemic gate requires a source/version/scope and revision condition for changeable procedural claims, a distinction between tested rules and hypotheses, and checks for instance answers embedded as reusable advice. A plausible warning inferred from one failure must not become a permanent universal prohibition without evidence. Preserve rejected/uncertain claims for review in the research record, not as operative instructions in the generated artifact.

### 6.5 Zero observed failures is not a guarantee

**Illustrative calculation:** under independent identically distributed Bernoulli trials, with zero observed failures in `n` trials, a one-sided 95% upper confidence bound on failure probability is `1 - 0.05^(1/n)`. It is about 13.9% for 20 trials, 3.0% for 100, and 1.0% for 300.

Those assumptions fail if the scenarios are near-duplicates or omit entire failure classes. The calculation therefore cannot certify safety; it demonstrates why “passed our small suite” is much weaker than “rarely fails.” Severity-based review and adversarial testing remain necessary, and neither establishes an absolute guarantee.

## 7. Efficiency and maintainability belong in the judgment

### 7.1 Measure cost at the boundary the user pays for

Record model tokens by category where available, tool charges, elapsed time, retries, user interruptions, review effort, and failure recovery. Distinguish warm and cold caches if they materially change the result. A shorter instruction file can produce a longer, more confused execution.

Do not optimize raw tool-call count in isolation. One extra verification call may prevent expensive rework. Conversely, ritual checking may consume time without changing a decision. Judge a step by the information or risk reduction it contributes.

Choose the accounting perspective before charging costs:

- **A user's adoption decision:** incremental future installation, migration, validation, operation, human review, incidents, updates, and retirement over horizon `H`. Include all catalog-visible traffic, not only invocations.
- **Creator-method comparison:** every allowed generation attempt, research/clarification, selection, debugging, and creation-time feedback. Report common external evaluation cost separately; charge candidate-specific evaluation it uses to select an output.
- **Research-program cost:** building this project and benchmark is a separate investment. Do not allocate all of it to each generated skill or invent a competitor's historical research costs as per-use expense.

Keep tokens, money, elapsed time, and human minutes separate unless the decision owner approves conversions. Count costs once: either inside an explicitly defined net utility or in a separate cost term, never both. A prospective accounting model is:

`incremental value_H = N_e * b - N_all * a - F`,

where `F` is incremental setup/validation/maintenance/retirement cost, `b` is net benefit per eligible episode after its variable execution/review/recovery costs, and `a` is catalog/selection overhead on every request, including eligible ones. All quantities must share defensible units for subtraction. Use a more detailed model if eligibility, overhead, failure rates, or benefits vary with time. Forecast use as a range; sunk costs do not become avoidable merely by allocating them differently.

If all-traffic overhead is already included in net eligible benefit `b_net>0`, break-even eligible uses are `F/b_net` (round up for indivisible uses). If `b_net<=0` and `F>0`, no finite number of uses repays setup under the model. This is not a statistical superiority test. See the low-risk example in section 10.

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

Anthropic explicitly describes holding selection scores out of improvement feedback while choosing the best iteration on those scores. This is legitimate validation selection; no inspected passage claims its selected maximum is an unbiased deployment estimate. Our narrower objection concerns using that maximum as final confirmation. Independent testing or a justified selection-aware design is needed for that additional claim. The [audit](research/implementation-audit.md#21-the-split-called-test-is-used-for-selection) provides the code and a selection-optimism counterexample. [M2](research/source-register.md#m2-model-selection-bias)

The audit also identifies a static shared-catalog risk in concurrent trigger probes, early-routing limitations, and conflation of worker errors with non-triggering. These are instrument concerns, not measured performance deficits. Preserve the exact native baseline; any repaired probe is a separately labeled diagnostic, or all methods use a common external evaluator. We have not run these probes.

### 8.2 Direct skill experiments are relevant but provisional

The source register now makes version and claim-level dispositions explicit. These studies are paper-reported evidence, not results reproduced here:

- **SkillsBench:** historical v1 and the current v4 are kept separate. The current aggregate, selection rules, and generated-skill caveats are recorded once in [D1](research/source-register.md#d1-skillsbench). Neither version estimates deployment-wide benefit or isolates a universal optimum for length/module count. Do not count versions as replications.
- **SWE-Skills-Bench:** retain as a qualified lead, with unresolved loading and raw-data access. Its cost-efficiency ratio is unsuitable as a general decision rule. Do not treat a small reported average as equivalence or use it to set this project's expected effect. [D2](research/source-register.md#d2-swe-skills-bench)
- **SkillLearnBench:** useful for studying authoring/feedback and downstream measurement; its adapted creator and reference-sensitive scores do not rank the complete pinned workflows or certify safety. [D3](research/source-register.md#d3-skilllearnbench)

**Synthesis:** remove all three preprints and the basic framework still stands: adequacy is distinct from comparative benefit; observed access is distinct from causal reliance; selection scores are distinct from independent confirmation; and budget/permissions define the intervention. Those conclusions rest on explicit counterexamples, inspected implementation contracts, and methodological sources, not on a pooled average. Direct studies motivate hypotheses about interactions among baseline competence, content, host integration, and task selection. The magnitude and prevalence of those effects remain open here.

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

Use an attempt ledger with case/family, creator/artifact identity, condition, start/stop, consumed budget, raw trace, outcome, censoring reason, and rerun linkage. Operational timeouts and budget exhaustion are outcomes of the policy, not discardable infrastructure noise. A verified external outage independent of the method may support a technical rerun under a predeclared rule; preserve the original. An ambiguous cause stays unknown and receives sensitivity analysis, not favorable reclassification. An invalid oracle requires regrading or invalidating the affected comparison, not blaming the solver. A crashed negative trigger test is not correct abstention.

R4 must operationalize this decision tree, including limits on retries and escalation after repeated failures. Report attempt-level operational success as primary where deployment includes the failure exposure; conditional healthy-infrastructure performance is supplementary. Report missingness and exclusions by arm. If unresolved outcomes can reverse the decision under plausible best/worst assignments, retain an inconclusive result.

### Stage D: Estimate effects, not just scores

Report paired outcome differences, per-task results, important strata, severe failures, costs, and uncertainty. Keep the unit of analysis honest: twenty variants of one template are not twenty independent task families. Repeated seeds reduce uncertainty about that task's behavior; they do not create new domain coverage.

Choose an uncertainty method suitable for the design. A task- or family-clustered bootstrap may suit a sufficiently broad sampled collection; exact paired methods or a justified hierarchical model may suit other designs. Very few clusters can make any population interval unstable. State assumptions and avoid substituting a standard deviation for a confidence interval on the effect.

Determine sample size from the decision, effect scale, risk tolerance, variation, and cost. A few pilot cases can find large defects; they cannot establish small differences or rare-event safety. Freeze confirmatory endpoints and handle multiple comparisons explicitly. State which uncertainty is being estimated: solver/environment variation on a fixed suite, variation between generated artifacts, sampling of downstream tasks, or transport across creation families. Repeated seeds cannot stand in for more families. For paired binary outcomes retain the discordant pairs; marginal pass rates alone omit relevant information.

Choose the claim before its margin: superiority, minimum-worthwhile superiority, noninferiority on quality with a cost benefit, or equivalence within a symmetric/asymmetric acceptable range. A nonsignificant difference is not a tie. The confidence interval must lie in the predeclared decision region for the associated inference. The owner chooses practical margins; the analysis method supplies uncertainty. Record the finite family of comparisons and subgroup claims, as well as adaptive choices of candidate, baseline, rubric, and stopping point. Multiplicity correction after unrestricted adaptation does not retroactively make the study confirmatory. If optional stopping is needed, use a valid sequential design rather than repeatedly checking until a favorable result appears.

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

Choose the evidence tier by the decision, potential harm, reversibility, and cost of being wrong:

| Tier | Required evidence and exit | Claim allowed |
|---|---|---|
| Development/smoke | Format/resource inspection, representative benign task, likely failure/boundary checks, declared limitations; fix obvious defects | Feasible example or development readiness, not adoption superiority |
| Bounded adoption | Adequacy on important uses, proportionate comparator check, critical invariants, prospective costs, restricted rollout/rollback, monitoring owner | Worth a limited reversible use under stated assumptions; inconclusive relative evidence remains inconclusive |
| Comparative research | Frozen methods/endpoints, faithful strong baselines, calibrated graders, enforced information boundary or valid selection-aware design, nested uncertainty, explicit margins | Scoped comparative inference supported by the actual design |

A tier is not an exemption from permissions or severe safety constraints. High-consequence, irreversible uses may require assurance this project cannot provide, independent expertise, or a decision not to deploy. Conversely, a small personal formatting aid does not automatically require a calibrated panel, long maintenance trial, and an independent custodian before any use.

At each tier, stop if evidence is invalid for the intended claim, severe violations remain, or the supported envelope cannot meet adequacy. Otherwise compare the expected value of more information with its cost. A cheap, reversible adoption trial can be reasonable without proving superiority. If uncertainty cannot be resolved within a sensible budget, narrow the claim, keep the incumbent, or stop evaluating. Do not turn every unknown into either a release ban or a win.

Publish the tested envelope, unresolved strata, rollback condition, and re-evaluation triggers. Numerical confidence levels and pass-rate thresholds are not universal release standards. R4 supplies defensible margins and costs for this project's actual stakes before confirmatory results exist.

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

### A proportionate low-risk decision

Consider a separate, deliberately low-risk use: formatting copies of personal, nonsensitive CSV exports, with originals read-only and a diff preview. This is a hypothetical accounting example, not the customer-data scenario's risk classification or a measured saving.

Assume one month has 200 total requests, 20 eligible uses, and 1.5 human minutes saved per eligible use after variable execution, review, and recovery. Assume catalog overhead costs 0.02 human-minute-equivalent per request and the owner accepts that conversion. Setup plus expected maintenance costs 8 minutes. Set an explicit additional evaluation ceiling of 5 minutes after the minimum permission/preservation checks; if those checks cannot fit, stop or keep the simpler script rather than waive them.

At that ceiling, `F=13` minutes and projected net benefit is `20*1.5 - 200*0.02 - 13 = 13` minutes. At a stable 10% eligible rate, all-traffic overhead is `0.02/0.10=0.2` minutes per eligible use, so `b_net=1.3`; break-even is `13/1.3=10` eligible uses. This forecast can support a limited reversible trial with manual preview, not a superiority claim or a rare-failure bound.

If only six eligible uses are likely at the same traffic mix, value becomes `6*1.5 - 60*0.02 - 13 = -5.2` minutes. Retain the existing script. If an observed preservation defect appears, stop even if the time model is positive. More expensive evaluation would not rescue a clearly unfavorable low-volume decision unless it addresses a separate consequential risk. None of these numbers is a recommended universal budget or threshold.

## 11. What would make a skill-creation skill superior?

### 11.1 Evaluate the complete creator policy

The object is the creation process, not its prettiest surviving file. Let `B` be a creation brief sampled from declared population `P`; `E_B` the legitimately available requirements, references, clarifications, and development feedback; and `R_c` creation randomness. A frozen method `m`, including its resource cap, retry/selection policy, human-help policy, and host adapter, returns:

`A_m = F_m(B, E_B, R_c)`,

where `A_m` is an artifact or an explicit alternative/abstention/failure status. Its produced artifact is then evaluated by a fixed downstream solver on new episodes `X ~ D_B` with solver randomness `R_s`. A skill-generator estimand can be the expected authorized downstream success, counting invalid/no-artifact creation as zero:

`G_m = E_{B ~ P, R_c, X ~ D_B, R_s}[q(Y(A_m, X, R_s))].`

The **authoring-assistant** comparison is broader. Let `pi(A_m)` be the predeclared deployment/fallback policy for the returned status, `N_B(H)` the forecast episode count over horizon `H`, `u_B` gross outcome utility in approved common units, and `K_m(B,R_c,H)` expected total prospective creation, selection, setup, operation, review, recovery, catalog, and maintenance costs in those same units. Then:

`V_m(H) = E_{B,R_c}[sum_{j=1}^{N_B(H)} E_{X_j ~ D_B,R_s} u_B(Y(pi(A_m),X_j,R_s)) - K_m(B,R_c,H)]`.

Compare `V_m - V_baseline` over the same briefs and horizon. Without agreed conversions, report outcome/cost vectors rather than evaluate this scalar. Hard constraints remain outside compensating averages. This corrects a potential ambiguity in the critic's per-episode utility minus horizon-cost notation: both terms now share the same horizon.

Two claims are therefore distinct: generation quality `G_m` and end-to-end authoring value `V_m`. R4 must designate one primary claim, not switch after seeing which wins. Report routing quality, production/failure rates, and conditional artifact quality alongside it. Good advice to reuse a tool can succeed as authoring assistance without being a produced skill; blanket abstention cannot win by removing hard briefs.

### 11.2 Failures, help, selection, and weights

- **No artifact, invalid package, unsupported dependency, or cap breach:** retain the assigned brief in the denominator with status and spent cost. For `G_m`, no usable generated artifact scores zero. For `V_m`, apply an identical predeclared fallback, normally the feasible incumbent, and charge wasted creation cost; do not pretend failed creation produced the fallback. If no fallback is feasible, score the specified noncompletion outcome. Report hard violations separately.
- **Appropriate alternative or abstention:** score the downstream value of the approved recommendation/fallback and the correctness of routing, judged against independently stated requirements. Clarification/unsupported cases can be correct boundaries, but do not disappear from coverage or production reporting.
- **Human assistance:** use the same available answer bank/domain reference access and clarification budget. A frozen facilitator policy may answer unforeseen questions without seeing arm identity; record all answers and time. Richer human help in one arm is a different human-plus-creator system.
- **Multiple attempts:** select with the frozen policy and permitted development data, charging every attempt and selection call. Never choose the best artifact using final downstream scores. A single generation and a best-of-five procedure are different interventions.
- **Weighting and units:** give each brief/family its predeclared weight, then average downstream instances and solver repeats inside artifact/brief as designed. Do not let a brief with more generated artifacts or cheap tests acquire accidental weight. For generality across families, families are the outer sampling unit; artifacts are nested within briefs, downstream episodes within their deployment population, and repeated solver trials within episodes. Shared repositories/templates may require additional clustering.
- **Native versus adapted baselines:** pinned OpenAI and Anthropic workflows plus a strong concise-prompt baseline remain proposed comparators. A native model-host-workflow comparison estimates system value. A common-model/adapter comparison estimates adapted method value and must disclose changed capabilities. One cannot substitute for the other. No host/budget fairness has yet been demonstrated.

### 11.3 Staged information boundary

| Stage | Creator/developer may see | Solver may see | Kept out of creation/selection access |
|---|---|---|---|
| Method development | Public research, training briefs, development tasks and feedback | Development tasks for diagnostics | Future evaluation-family briefs and downstream confirmation instances |
| Freeze method; reveal new brief | Legitimate brief, permitted references, answer-bank clarifications, predeclared development examples | Only authorized creation-time diagnostics, counted in budget | Independently owned downstream holdout instances, solutions, secret grader tests |
| Freeze selected artifact and adapter | Artifact digest and creation ledger; no final-score-driven revision | Its assigned task, ordinary input data, package/resources, permitted tools | Oracle solutions, grading secrets, other arms' artifacts/results |
| External grading | Locked outputs/traces for adjudication under fixed policy | No grading secrets or new coaching | No tuning on confirmation results |
| After decision | Final results may become development evidence for a subsequent version | Ordinary authorized tasks | A subsequent confirmatory claim needs new protection or a justified selection-aware design |

The first boundary protects a frozen creator against evaluation-family adaptation; the second protects each generated artifact against downstream-instance adaptation. A creator may see the information a real request supplies, but that does not mean it may inspect final test answers. The downstream solver must see its actual task and input at execution time.

An independent authorized custodian or enforced access separation must own concealed data, verify no shared workspace/memory/cache exposure, and record access and artifact digests. A promise not to peek, a fresh conversation, or a digest alone does not enforce concealment. This project currently has **no sealed holdout or custodian**. If that cannot be arranged, run an explicitly exploratory public evaluation and limit the claim. R4 must not label a fictional boundary as established.

Success would mean a bounded gain or quality-cost tradeoff under these pinned systems, budgets, sampled families, and constraints, with stated uncertainty and disclosed losses. It would not establish superiority to every present or future creator. The method must be allowed to tie, lose, recommend a simpler artifact, or remain unproven.

## 12. Conclusions and unresolved questions

The central claim is simple: **evaluate the change a skill causes, for the users and conditions that matter**. Everything else follows from taking that sentence seriously.

1. Artifact inspection supplies hypotheses and catches defects; it cannot establish marginal usefulness.
2. Selection and execution need separate diagnostics and a combined deployment test.
3. The task distribution, comparator, constraints, and measurement validity determine what a score means.
4. Reliability and safety require traces, repeated trials, adverse conditions, and explicit uncertainty.
5. Concision, modularity, and detailed procedure are contingent design choices.
6. A creator's quality is ultimately about the skills it produces under fair resource and information constraints.

R3 resolves the conceptual revisions but does not close empirical or value decisions by prose. R4 must choose target creation families and user goals, real host configurations, primary estimand, affordable budget/horizon, safety gates, grader calibration plan, information custodian or exploratory status, and an uncertainty/selection protocol. No universal sample size or release margin is supplied here. The next task is the fresh-context comparative-protocol design in [HANDOFF.md](HANDOFF.md), before creator implementation or paid experiments.
