# Independent critique of the skill-quality foundations

Date: **2026-10-02 UTC**. Stage: **R2**. Reviewed project commit: [`9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8`](https://github.com/danrjoyce/skills/commit/9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8).

## Verdict

**Retain the foundations, but revise before freezing the measurement model or designing the comparison.** The draft's central distinction between artifact appearance and demonstrated usefulness is sound. Its treatment of uncertainty is substantially better than a checklist-based quality score. The important failures are operational, not a collapse of the overall argument:

1. The definition makes being good require beating the best alternative. That confuses adequacy, usefulness, and superiority, despite distinguishing them later.
2. The intended callable product and runtime contract remain undefined. A skill package does not automatically register a native tool.
3. The evidence review misses a consequential revision of SkillsBench and needs stricter claim-by-claim admission decisions.
4. The Anthropic selection-set critique is correct but must remain fair to the implementation's stated purpose. A newly identified shared-directory interference risk is more actionable than repeating the generic warning about overfitting.
5. The proposed creator comparison needs an explicit nested estimand, information boundary, and accounting for unsuccessful creation, human help, and non-skill outcomes.
6. The protocol needs risk-proportionate tiers and a decision rule that can distinguish a tie, an unknown result, an acceptable alternative, and a demonstrated win.

No numerical error was found in the draft's illustrative precision or zero-failure calculations. No examined source establishes that a new creator is superior, or that either pinned public creator is generally poor. No model-performance experiment was performed in this review.

## Review scope and evidence standard

I read the main analysis, all supporting project files, repository guidance, and the repository's invocation convention. The nine starting project files matched their remotely fetched Git blob identities. All nine implementation-file blob SHAs in the R1 manifest matched independently fetched files at the pinned commits. Consequential branches were inspected directly rather than accepted from the audit's paraphrases.

The review also checked primary texts for measurement validity, interactive retrieval, selection bias, reliability, prompt injection, judging, contamination, and the direct skill studies. Additional discovery included the current arXiv version histories, the SkillsBench v4 methods, and the pinned Agent Skills integration guide. This is a targeted independent audit, not an exhaustive literature review or replication.

Classification used below:

- **P1:** resolve in R3 before committing to the R4 measurement and comparison design.
- **P2:** revise the framework now; make the specified implementation or numerical choice in R4.
- **P3:** useful improvement, not a gate on progress.
- **Factual/source issue:** a verifiable claim, omission, or source-interpretation problem.
- **Methodological issue:** the proposed evidence does not yet identify the intended claim.
- **Value/scope choice:** reasonable alternatives exist; the choice needs an owner and rationale.

An acceptance criterion below is a check on the revision, not a claim that the corresponding empirical work is already complete.

## C1. Good, worth adopting, and best must be different predicates

**Priority/type:** P1, conceptual and value/scope issue.

**Anchors:** main analysis, opening definition; sections 1.2, 1.3, 2.1, and Stage F.

The opening requires a good skill to outperform the best relevant alternative. Consider two independently authored skills that have identical, excellent outcomes and costs. Neither strictly outperforms the other. The definition would deny both the label good, even though either is fit for the user's purpose. Similarly, a reliable backup implementation can be valuable for resilience without beating the primary on average. An excellent existing skill does not become defective merely because a slightly better competitor appears.

This is not solved by the later, correct distinction between works, helps, and should be used. The opening currently collapses those distinctions again. Best also quantifies over an unspecified set of feasible alternatives; finding the true best alternative may itself be intractable. Comparing with a strong, declared comparator supports a relative claim, not a global optimum.

Legitimate goals and unacceptable effects are necessary normative terms, but are not supplied by outcome statistics. The relevant user's preferences, organizational requirements, affected parties, and non-negotiable constraints need an explicit place in the contract. Satisfying an immediate request is not automatically the entire welfare criterion. An unauthorized but accurate output cannot compensate for the authorization failure by earning enough style points.

**Revision:** distinguish:

- **Fitness for purpose:** meets declared outcome and constraint requirements in the supported use envelope.
- **Incremental value:** improves a declared alternative, or offers an acceptable tradeoff.
- **Adoption decision:** expected prospective benefits justify costs and risks for this user and horizon.
- **Comparative superiority:** exceeds named alternatives under the stated experiment and decision rule.

Keep quality as a vector of properties and uncertainty. Use a Pareto comparison when benefits are not commensurable. If a scalar utility is used, identify who chose its weights, its units, and sensitivity to plausible alternatives. Do not use failure to find a significant difference as evidence of equivalence.

**Acceptance:** the revised definition admits equally good alternatives; identifies the comparator set without requiring an omniscient optimum; and supplies a small decision table for adequate, beneficial, dominated, unsafe, and unknown cases. A tie does not become a failed artifact or an invented win.

## C2. Specify the callable product and distinguish package portability from execution portability

**Priority/type:** P1, factual/runtime scope issue.

**Anchors:** main sections 1.1, 4, 5, and 11; methodology section 6; repository [invocation convention](https://github.com/danrjoyce/skills/blob/9283609fbd998aeb3a4de2e00e41d73d0bfd5cf8/.agents/invocation.md).

The draft correctly says a package is not a capability, but does not cash that out for the proposed general-purpose call-tool. At least three products fit that phrase:

1. A skill whose instructions an existing host skill-loader makes available to an agent.
2. A CLI or script that an existing execution tool runs.
3. A native function-calling tool or MCP service with a registered schema and an implementation.

These are different deliverables. Creating `SKILL.md`, a script, or a manifest does not by itself add a new callable tool to an arbitrary model's tool inventory. Nor does naming a tool in prose make it exist. A loader that returns instructions is also not necessarily a function that executes the entire skill and returns a typed result.

The pinned [integration guide, activation section](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/client-implementation/adding-skills-support.mdx#L234-L260) explicitly distinguishes file-read activation from a dedicated activation tool that the host registers. The guide also describes user-explicit injection and optional subagent execution. Its blob is `6c784309faec4ea27715e57734e1e0b5929c1977`, independently retrieved in R2. The [format specification](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx#L23-L32) describes environment compatibility and an experimental tool allowance field; neither is a universal tool registration contract.

The repository's instruction to call a named Skill tool is a local invocation convention, not evidence that every target host exposes that exact interface. Likewise, user-invoked-only packages must not be penalized for failing autonomous activation. Their human-facing discovery and explicit invocation should be tested instead. A cross-host adapter is part of the intervention and must not be hidden in the comparison.

**Revision:** declare the initial deliverable and supported host envelope. A reasonable research scope is a reusable creation workflow with documented host adapters, while leaving a separately registered service out of scope unless intentionally chosen. Record installation/discovery, explicit versus model invocation, resource path resolution, executable dependencies, permission behavior, output contract, and failure/unsupported-host behavior.

**Acceptance:** a reader can answer how the creator and each generated artifact are invoked on each claimed host, what component registers any tool, and who executes scripts. Include a negative compatibility case: a parseable package on a host without the required loader or executor. Mark untested hosts untested. Do not change repository-wide invocation rules as part of this research revision.

## C3. Tighten source admission and reconcile versions before carrying forward headline results

**Priority/type:** P1, factual/source and evidence-triage issue.

**Anchors:** main section 8.2; source register D1-D3 and M3; methodology sections 2-3.

The evidence hierarchy is sensible, but the practice needs a claim-level disposition: retain as direct evidence, retain as a hypothesis, exclude from a particular inference, or await verification. Primary authorship establishes provenance, not validity. Source code establishes a possible or actual code path, not its deployment frequency. A preprint with a clear experiment can be useful, but does not become replicated evidence through multiple citations.

### D1: the v1 summary is historical, not the current evidence snapshot

The [arXiv history](https://arxiv.org/abs/2602.12670) lists v4 dated 14 June 2026, well before this review. R1's v1 account is correctly pinned but omits the major update. The [v4 abstract and sections 4-5](https://arxiv.org/html/2602.12670v4) report 87 tasks, 18 configurations, and a 16.6-point aggregate increase. More importantly, v4 changes the setup and discusses creator/solver interference and missed discovery in generated-skill runs. Appendix N selects healthy verifier-scored runs ahead of timeout backfills; Appendix G uses result-count-based Wald intervals. These choices need scrutiny, not automatic promotion of the newest headline to a trusted effect estimate.

**Disposition:** retain v1 only with its historical scope; reconcile v4's population, run selection, and generated-skill setup. The reported intervals do not directly establish a paired, task-clustered treatment-effect interval. Neither version establishes a universal package-size optimum or ranks the exact pinned creators under this project's proposed protocol. Do not combine their samples as independent replications.

### D2: weaker than the current summary's prominence suggests

The [paper's sections 3.2 and 4.1](https://arxiv.org/html/2603.15401v1) do give conflicting skill-placement accounts. Its linked [repository](https://github.com/GeniusHTX/SWE-Skills-Bench) returned 404 through both web retrieval and the GitHub API on this review date; this does not establish why it is unavailable. Actual loading and raw results remain unverified.

Equation 5's cost-efficiency ratio also has a sign problem: positive accuracy change divided by negative cost change is negative despite being an improvement on both dimensions; two negative changes give a positive ratio despite worse accuracy. The verbal interpretation cannot hold generally. This is a problem in the source, not an arithmetic error already imported by R1.

**Disposition:** retain as a qualified reported observation and a lead for verification. Exclude the ratio as a decision rule. Do not use its near-null average to establish that skills are generally ineffective or powered equivalence. Restore access and inspect loading, trial-level data, weighting, and uncertainty before using its quantitative result to calibrate this project's expected effect or budget.

### D3: useful process evidence, not a full-creator leaderboard

The [methods and Appendix M](https://arxiv.org/html/2604.20087v1) confirm the skill-dependent selection, 17 adapted SkillsBench tasks, and the single-round creator condition. R1's caveats survive. Its artifact and trajectory scores reward agreement with reference skills or oracle steps, so efficient valid alternatives may receive lower process scores.

**Disposition:** retain for hypotheses and protocol design. Do not treat reference similarity as demonstrated usefulness, textual safety scores as behavioral assurance, or this adaptation as a ranking of the complete pinned Anthropic creator. The overlap is evidence dependence, not replication.

### Established methodological sources

The direct claims checked in [Jacobs and Wallach](https://arxiv.org/html/1912.05511v3), [Cawley and Talbot](https://jmlr.org/papers/v11/cawley10a.html), [tau-bench](https://arxiv.org/html/2406.12045v1), [AgentDojo](https://arxiv.org/html/2406.13352v1), [LLM-as-a-judge](https://arxiv.org/html/2306.05685v4), and [Oren et al.](https://arxiv.org/html/2310.17623v2) support the bounded methodological uses made of them. None validates a universal skill-quality scale. The [Borlund paper](https://informationr.net/ir/8-3/paper152.html) supports contextual relevance as an analogy; it does not validate an agent activation benchmark.

The TMLR [publication record for AI Agents That Matter](https://openreview.net/forum?id=Zy4uFzMviZ) is a useful source-upgrade lead. Its PDF again encountered an OpenReview browser-verification page here. R1 was right not to pretend that the accessible [preprint](https://arxiv.org/html/2407.01502v1) and final version had been compared. Preserve that retrieval limit unless R3 actually resolves it.

**Acceptance:** add an explicit source-version and claim-disposition record. Preserve the valid methodological conclusions if all three direct preprints are removed. Separate paper-reported results, independently reproduced results, source-code observations, and proposed design choices. There is still no independent reproduction in this project.

## C4. Preserve the fair Anthropic critique, and add the more concrete probe-integrity risks

**Priority/type:** P1, implementation and inference issue.

**Anchors:** implementation audit sections 2.1-2.3; main section 8.1. All code links below use Anthropic commit `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`.

### What is confirmed

The draft's central source claim is correct:

- [`run_loop.py` lines 24-44](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L24-L44) stratify the split.
- [Lines 86-119](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L86-L119) evaluate both partitions.
- [Lines 194-208](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L194-L208) remove test-prefixed history and pass training results to the improvement function.
- [Lines 216-234](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L216-L234) select and report the best test-scoring iteration.

The authors explicitly describe that selection in [the creator's optimization instructions](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/SKILL.md#L375-L404). This is ordinary validation-set selection intended to reduce overfitting to training feedback. It is not concealed leakage into the improvement prompt. No inspected passage claims that the selected score is a calibrated, unbiased estimate of future deployment performance. The critique should identify the limit on that additional inference rather than refute a claim the authors did not make.

A minimal mathematical counterexample establishes why the limit matters: two equally capable candidates each have true success probability 0.5, and each gets one independent binary validation observation. The expected maximum observed score is 0.75, while the selected candidate's success probability remains 0.5. This is an illustration, not an estimate of bias in this optimizer. Selection optimism is not inevitable or of fixed size; identical correlated scores or only one candidate can eliminate this particular effect. The code also stops when the training queries all pass, so it does not necessarily evaluate five candidates.

An independent final evaluation is the simplest recommendation for this project's intended claim. It is not the only statistically possible design: a justified nested or selection-aware procedure could support a bounded claim too. Do not characterize normal model selection as misconduct or require every practical development loop to become a full confirmatory study.

### Additional static issue: concurrent probes share a changing catalog

[`run_eval.py` lines 51-89](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L51-L89) give each probe a unique command filename but write every command into the same project `.claude/commands` directory. [Lines 198-211](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L198-L211) submit these probes concurrently with that shared project root. The loop defaults to ten workers and three runs per query. Detection only accepts the probe's own generated name.

A feasible interleaving is: probe A writes command A; probe B writes command B with the same description; both subprocesses discover both commands; B chooses A; B's detector reports non-triggering because its expected identifier was B. Deletion by another probe can also change available resources during execution. Unique filenames prevent an overwrite, but do not isolate the catalog.

This establishes a **static interference risk**, conditional on the CLI discovering overlapping command files as intended. It does not establish its observed frequency or effect size. The actual CLI version, discovery timing, catalog contents, and installed original skill were not tested here. A single-worker versus isolated-multiworker diagnostic and catalog snapshots are warranted before treating the probe as an experimental instrument.

### Other confirmed limits, with appropriate weight

- The minimal temporary body and early exits in [lines 51-68 and 128-178](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L51-L178) support an early selection probe. Calling another tool first can legitimately precede later skill access, so the metric is not general multi-turn discovery.
- Worker exceptions become `False` in [lines 221-234](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L221-L234), which can help a negative case pass. Technical failure and appropriate abstention must be distinct.
- With three repeated probes and threshold 0.5, the reported query pass is majority success, not the probability of correct activation on one request. Under independent per-run correctness `p`, majority correctness is `3p^2 - 2p^3`. For illustrative `p = 0.9`, it is 0.972. Report raw counts alongside thresholded query scores.
- Query text is used as the aggregation/split key, rather than a unique case ID. Exact duplicate text, especially with inconsistent labels or across partitions, needs validation before using this harness. This is a preflight requirement, not evidence that the authors' supplied cases were duplicated.

**Baseline fairness:** preserve the original workflow as the native baseline. If probe-integrity repairs are needed, document an additional repaired-harness condition or a common external evaluator; do not silently handicap the public baseline or present its known measurement artifacts as a victory for a new creator. Its human review and blind-comparison machinery remain genuine strengths.

**Acceptance:** retain the selection-set observation with the authors' actual intended claim; add an instrument contract and test plan covering shared catalog interference, exceptions, delayed activation, duplicate cases, and raw-versus-thresholded scoring. Distinguish verified code paths from unmeasured runtime consequences. Do not edit upstream code or run a paid benchmark during R3 merely to close this conceptual review.

## C5. Finish the causal and creator estimands, including failures and the information boundary

**Priority/type:** P1, methodological issue.

**Anchors:** main sections 3.1-3.3, 5, Stage E, and 11.

The deployment estimand is directionally correct, but `Y(1, X)` should explicitly include agent and environment randomness, or be defined as an expectation over it. Pairing episodes controls the initial case; it does not magically observe both potential outcomes in one live world. Nor does a convenience sample become representative because a clustered bootstrap is applied. A finite-suite effect and an effect transported to an intended population are different claims.

Forced use also changes the intervention. Injecting the body, issuing an explicit instruction to use it, and allowing normal loading are not equivalent. Their effects on attention and budget differ. A forced-loading experiment is a diagnostic, not a direct estimate of what the naturally activated subset would have achieved under the opposite condition. The draft already rejects that post-selection comparison; make the operational alternatives equally explicit.

For creator comparisons, define the complete procedure, not just an output file. A compact proposed notation is:

`A_m = F_m(B, E, R_c)`

`V_m(B) = E_{R_c, X ~ D_B, R_s}[u(Y(A_m, X, R_s))] - K_m(B, H)`

Here `B` is the creation brief, `E` the permitted evidence and feedback, `R_c` creation randomness, `D_B` the downstream population, `R_s` execution randomness, and `K_m` the prospective costs allocated over horizon `H`, in the same units as utility if subtraction is justified. Otherwise report cost and utility separately. Compare `V_m - V_baseline` over a declared distribution of briefs. Hard safety constraints remain outside compensating averages.

This notation forces currently missing decisions:

- What happens when a creator delivers no artifact, an invalid package, an over-budget artifact, or an unsupported dependency? These outcomes belong in the denominator.
- If a correct recommendation is a script, reference, or no new skill, is the evaluated object a skill generator conditional on production, or a broader authoring assistant? Report routing quality and conditional artifact quality separately; score end-to-end value without rewarding blanket abstention.
- How are human clarifications and expert feedback supplied? The human is part of the creation process. Give comparable access to predeclared answers and account for effort; do not let one arm receive richer undocumented help.
- Does a native-runtime comparison include a different underlying model? If so, it estimates a creator-model-runtime system comparison. An adapted same-model comparison answers a different question and needs its own label.
- Do multiple generation attempts produce several artifacts, and is the best chosen? Charge and evaluate the entire selection policy. Testing only the best surviving artifact understates failure and cost.

There are two relevant concealment boundaries. Freeze the creator before exposing new creation-family briefs for evaluation; allow it the information a real creation request would legitimately provide. Then freeze each generated artifact before exposing its independently held-out downstream instances and grading secrets. The downstream solver must see its task and ordinary inputs at execution time. Hiding all downstream information permanently would make execution impossible; hiding solutions and graders is the important distinction. Separate conversations alone do not enforce either boundary.

**Acceptance:** provide one explicit skill-level estimand and one creator-level estimand; define failure, abstention, information access, selection policy, weighting, and analysis units; distinguish native system comparison from adapted method comparison. Include a staged information-flow diagram or table and state which boundary can actually be enforced. If concealment cannot be enforced, label the exercise exploratory instead of describing an imaginary sealed test.

## C6. Make measurements observable and calibrate the evaluator, not just the solver

**Priority/type:** P2, measurement and information-science issue.

**Anchors:** main sections 2.1-2.2, 4.1-4.3, 6.1, and Stage B.

The multidimensional model avoids an unjustified latent quality scale. Preserve that strength. But it mixes desired outcomes, causal effects, diagnostics, and maintenance properties in one list without specifying how each will be observed. A trace can establish that content was loaded, a script ran, or an output satisfied a check. It cannot directly establish that the model understood the skill. Successful output could reflect pre-existing capability; a self-report of skill use is not a causal test.

Likewise, reliability of the agent and reliability of the measurement instrument are different. Rerun the grader on fixed outputs separately from rerunning the solver. Agreement among graders that share the same faulty oracle is not independent validation. The distinction follows the measurement source's warning about agreement between insufficiently validated measures, but the proposed application remains this project's responsibility.

Activation relevance is contextual and sometimes graded. A skill can be useful after inspecting an input, unnecessary for an easy instance, or one of several acceptable choices. A binary immediate-trigger label may confuse harmless delay, reasonable substitution, prohibited use, and unsupported use. The information-retrieval analogy supports taking context seriously; it does not imply a unique ground-truth label for every request.

**Revision:** operationalize observable events and score appropriate alternatives. Predefine the activation time window, invocation mode, acceptable substitute skills, ambiguity handling, and which cases leave the denominator. Report that coverage. Use deterministic oracles where valid, adversarial negative controls, independently checked reference artifacts, and human calibration for contextual quality. Distinguish critical false passes from cosmetic disagreement; generic inter-rater agreement can hide the former. A grader detecting 99 easy defects does not compensate for missing the one authorization violation.

Do not turn the draft's custom validity questions into claims of having implemented an established psychometric scale. In particular, its discrimination question means sensitivity to meaningful improvements, not the technical discriminant-validity construct discussed in M1. Its prediction question is a deployment validation proposal, not a literal restatement of every source's predictive-validity definition.

**Acceptance:** add a metric-to-observable mapping with units, oracle, adversarial counterexample, uncertainty source, and permissible inference. Replace unobservable understanding claims with trace-based diagnostics. Specify separate grader-repeatability, substantive-validity, and solver-reliability checks. Include at least one valid noncanonical solution and one appropriately delayed or substituted activation.

## C7. Make evaluation cost and release gates proportionate to the decision

**Priority/type:** P2, value/scope and accounting issue.

**Anchors:** main sections 7.1-7.3 and Stage F; methodology section 6.

The draft may be read as requiring a full comparative study, independent custodian, calibrated panel, adversarial testing, maintenance trial, and population uncertainty analysis before any skill can be useful. That can defeat a low-risk skill that saves minutes on a reversible personal task. Conversely, a high-impact automation needs stronger assurance than a large average score. Risk proportionality needs to be an executable rule, not just a caveat at the end.

Separate three levels: development/smoke checks; a bounded adoption decision with proportionate verification and rollback; and a comparative research claim requiring a frozen evaluation. No level should fabricate superiority. An inconclusive small experiment can justify more information or a limited reversible trial, rather than either a sweeping release block or a positive claim.

The lifecycle expression is valid bookkeeping but omits its accounting boundary. Catalog costs accrue even when a skill is not invoked. Installation, migration, user review, false activations, verification, incident recovery, and retirement can matter. The fixed cost of building this research project should not be charged to every generated skill, nor should a competitor's sunk historical research be invented as a per-use expense. Algorithm comparisons, creator customization, and a user's adoption decision have different relevant costs.

For a simple illustrative break-even calculation, let `F` be incremental prospective setup and maintenance cost and `b` expected net benefit per eligible episode after variable costs. If `b > 0` and rates stay stable, break-even uses are `F / b`; if `b <= 0`, no finite number of uses repays `F` under that model. Include noneligible traffic separately when catalog overhead is paid on all requests. Keep human time, money, and latency separate unless the conversion is justified.

**Acceptance:** include a tiered decision procedure and a worked low-risk example with an evaluation-cost ceiling. Define cost perspective, horizon, units, uncertain use frequency, and all-traffic versus invoked-traffic costs. Show a case where the correct decision is to stop evaluating or retain a simpler solution. R4 can supply numeric thresholds after pilot variance and practical budget are known.

## C8. Clarify missing-data rules and what uncertainty can establish

**Priority/type:** P2, statistical design issue.

**Anchors:** main sections 3, 6.4, and Stages C-D.

The draft correctly calls for preserving failed attempts, pairing, clustering, and valid stopping. Two details are still important:

- An operational timeout can be an outcome caused by the skill. Excluding it as infrastructure failure can select away the very cost of excessive procedure. Separate attempt-level operational success from conditional success when infrastructure is healthy. Define external outage and permitted technical rerun rules before outcomes; report exclusions by arm and sensitivity to them.
- An interval over repeated seeds on fixed tasks describes different uncertainty from an interval over sampled task families or generated artifacts. These cannot be substituted. More seeds do not resolve an unrepresentative brief population. Paired success margins also require the discordant cases, not only aggregate pass rates.

A non-significant improvement does not demonstrate a tie; a significant difference need not be worth adopting. Noninferiority, equivalence, superiority, and a quality-cost tradeoff need different margins and decisions. Correcting multiple comparisons is not enough if the candidate, baseline, subgroup, and rubric were all adaptively chosen. Record those choices and the finite family of claims.

The zero-failure calculation survives: its one-sided 95% limits are approximately 13.91%, 2.95%, and 0.994% for 20, 100, and 300 independent identical-risk trials. Its population assumptions matter more than the rounding. Missing entire risk classes is a coverage/transport problem; correlated scenarios are an independence problem. Neither is fixed by plugging a larger raw scenario count into the formula.

**Acceptance:** R3 distinguishes finite-suite, solver-randomness, creator-randomness, and population uncertainty. R4 must predeclare a timeout/rerun decision tree, retain an attempt ledger, select the pairing and clustering units, and state the decision margin and multiplicity family. Do not choose a universal sample count in the foundations document.

## C9. Expand safety from an execution checklist to a bounded assurance argument

**Priority/type:** P2, security and normative scope issue.

**Anchors:** main sections 6.2-6.4 and Stage F.

The safety section is strong on unauthorized mutations and untrusted task data. It needs a threat model for the skill package itself: untrusted authoring references can be laundered into apparently trusted instructions; scripts and dependencies can have effects outside the model's prose; installation, loading, and updates may change the trusted surface. The pinned integration guide's project-trust discussion reinforces that package content is a trust decision, not merely relevant context.

Specify assets, attacker control, ingress points, intended privileges, critical invariants, enforcement location, and residual risk. Test both benign completion and adversarial pressure. An agent that refuses everything is secure under a naive attack-success metric but useless. A skill that changes no final files can still leak data through a network request or expose secrets in logs. Do not make real credentials or live destructive operations a prerequisite for testing; use inert fixtures and controlled sinks.

The creator also needs an epistemic safety gate: can it turn an unverified claim into a confident reusable instruction, preserve unsupported warnings indefinitely, or embed task-specific answers that look like general guidance? This is both a correctness and a provenance risk. Factual references need authority, version, scope, and expiration conditions, not citation counts.

The phrase task data cannot authorize a new action should explicitly mean lower-trust embedded content cannot expand the user-approved scope. A direct user instruction or an already authorized machine-readable job request is not automatically untrusted merely because it is stored as data. Authority comes from the source and approved contract, not whether the bytes look like prose or JSON.

**Acceptance:** provide a concise creator-and-executor threat model, enforcement map, and benign/adversarial test pairs. Keep severe violations as noncompensating gates. Mark simulated assurance as simulated and never call zero observed failures a certification. Preserve provenance for newly generated procedural claims and a path to revise or retire them.

## Claims that survive scrutiny

These should be retained, not rewritten merely to demonstrate that a review happened:

- Quality depends on the artifact, agent, runtime, task population, constraints, comparator, and horizon.
- Format conformance and well-written instructions do not establish behavioral usefulness.
- Deployment, forced-use diagnostics, and component ablations answer different questions.
- Selection-set scores need a different interpretation from independent confirmation.
- Appropriate abstention, process constraints, cost, maintenance, and downstream effects matter.
- SkillsBench size associations do not establish a causal optimum; skill benchmarks cannot be pooled without compatible populations and interventions.
- User review and artifact-grounded evaluation in the Anthropic workflow are substantive strengths.
- The OpenAI validator discrepancies are accurately identified at its pinned version. It excludes `compatibility`, and empty stripped strings bypass the relevant branches. It is explicitly a minimal validator; this does not establish that the runtime accepts bad packages, that the complete authoring method is poor, or that full standards compliance is equivalent to runtime loading.
- The base-rate precision example is correct: `0.009 / 0.0585 = 0.153846...`.
- The reliability discussion correctly distinguishes `E[p_task^k]` from `(E[p_task])^k` and separates independent runs from stateful retry policies.
- The proposed rejection of universal best-creator claims is correct. A finite, scoped competition is testable; an open-ended claim to beat every creator, host, and future task is not.

## Unresolved empirical gaps

The review does not settle these by argument:

1. Which creation briefs and downstream uses matter enough to justify the creator, and with what prevalence?
2. How much benefit comes from instructions, scripts, extra information, host integration, or extra budget?
3. How often do the identified trigger-probe error and interference paths change measured decisions in the pinned runtime?
4. How well do human and automated graders detect consequential errors while accepting valid alternative outputs?
5. Which quality-cost and robustness tradeoffs persist across hosts, model upgrades, catalog growth, and time?
6. Can the project enforce a real final-evaluation information boundary, and who can own that boundary?
7. How often does the creator correctly choose a simpler artifact or no new skill, without using abstention to hide difficult cases?

These are R4-R6 questions after the conceptual revision. They are not reasons to implement a large process speculatively.

## R3 acceptance checklist and recommended order

1. Resolve C1-C2 first: define the product, supported invocation modes, quality predicates, and bounded ambition.
2. Reconcile C3 sources, preserving historical versions and avoiding unjustified upgrades of evidence strength.
3. Revise the implementation audit per C4 with fair purpose attribution and testable, explicitly static risks.
4. State the nested estimands and staged information boundaries in C5.
5. Add the observable metric map and risk-proportionate decision/accounting rules from C6-C9.
6. Write a response ledger for C1-C9: accepted and changed, rejected with evidence, or deliberately deferred to a named later stage. Do not mark an empirical gap solved by adding prose.
7. Leave numeric sample sizes, paid runs, and final release thresholds for the protocol stage. Do not create the final meta-skill yet.
8. Check internal consistency, citations, local links, arithmetic, unchanged repository scope, and remote publication. End with a precise R4 prompt and a list of decisions still requiring evidence or user input.

## Verification and limits of this review

- Read all nine R1 project files and compared their Git blob identities with the remote starting commit.
- Independently fetched all nine public implementation files in the R1 manifest; all blob SHAs matched. Added one pinned primary integration-guide source, identified above.
- Checked the source branches, paper passages, version records, and illustrative arithmetic described here.
- Rechecked the cited SWE-Skills-Bench repository through web retrieval and GitHub API; both returned 404. No conclusion about deletion, access policy, or research validity follows from that alone.
- The current TMLR PDF retrieval remained blocked by a browser-verification page. No final/preprint equivalence was assumed.
- Did not execute either creator, the validators, the description optimizer, a host compatibility test, a security experiment, or any cited benchmark. Code-interference examples are static counterexamples, not observed incident rates.
- Did not change the main analysis, source register, implementation audit, or source pins in R2. This artifact records the criticism for the separate revision task.
- Publication is limited to this critique and project tracking on the existing research branch and draft PR. No shipped skill, manifest, repository setting, merge, or upstream synchronization is part of R2.
