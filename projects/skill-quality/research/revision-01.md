# R3 response ledger and revised measurement framework

Date: **2026-10-02 UTC**. Starting project commit: [`ca27f690562c7440458dc50cdc0f01b5073f08ad`](https://github.com/danrjoyce/skills/commit/ca27f690562c7440458dc50cdc0f01b5073f08ad). Responds to [critique-01.md](critique-01.md), preserved unchanged. Scope: conceptual revision and source verification, not creator implementation or experimental results.

## Result

The [main analysis](../how-to-determine-if-a-skill-is-good.md) now separates adequacy, usefulness, adoption, and superiority; states an initial host-loaded product; formalizes nested creator evaluation; maps metrics to observables; and makes evaluation cost/risk proportional to the decision. C1-C9 each receive a reasoned disposition below. Their conceptual acceptance criteria are addressed. Their empirical questions remain open with named next steps.

There is no measured superiority, compatibility result, sealed test, calibrated grader, or implemented creator. A better-specified framework is a prerequisite for testing, not evidence that its authoring method works.

## Independent checks and approach

R3 read the repository guidance and all ten starting project files; their local bytes matched the remote starting commit. It independently fetched the nine originally pinned implementation files and the integration guide identified by R2. All ten returned the expected blob SHAs. Consequential code branches and author-facing descriptions were inspected, not merely the critic's interpretation.

The source review revisited exact paper versions and passages, including the current SkillsBench history and methods, the other direct skill studies, and the accessible methodological sources. The [source register](source-register.md) now records claim-level admission and excluded inferences. Retrieval failures remain failures: the SWE repository is not code evidence, and the unread TMLR final text is not silently substituted for its accessible preprint.

This was one sequential revision task in fresh context. It did not delegate parallel research, execute upstream code, spend on model tests, or change shipped skills.

## C1. Fitness, value, adoption, and superiority

**Disposition: accepted and revised.** The critic's equal-alternative counterexample defeats the original requirement that a good skill must beat the best alternative. No empirical source is needed to demonstrate the definition's logical problem. Both equally fit alternatives can be good; a dominant competitor can change the adoption choice without retroactively making the incumbent defective.

**Change:** main sections 1.2 and 9 Stage F now separate four predicates, identify decision owners and noncompensating constraints, and provide evidence-state and tiered-decision tables. Adequate, beneficial, equivalent-within-margins, dominated, unsafe, and unknown states no longer collapse into pass/fail. Comparators must be named and feasible rather than an unknowable global optimum. Vector/Pareto reporting is the default when utilities cannot be justified in common units.

**Limit/next step:** adequacy requirements, affected-party interests, acceptable margins, and the value of backup/portability still need the actual domain owner's judgment in R4. A table cannot supply those values. A nonsignificant difference is explicitly not equivalence.

## C2. Callable product and runtime envelope

**Disposition: accepted; initial scope choice recorded, runtime verification deferred.** The independently inspected [integration source S5](source-register.md#s5-agent-skills-client-integration-guide) supports the critic's package/host distinction. A native tool needs a host registration/implementation path; a file does not create one. The local invocation convention cannot prove a cross-host tool name.

**Change:** main section 1.4 chooses a host-loaded model-invocable authoring workflow as the initial candidate, not a new service. It describes target Claude Code/Codex native paths, an explicitly versioned adapter condition, a no-loader negative case, resource resolution, permissions, statuses, and deliverable evidence. The hosts are **targets, untested**, not verified supported configurations. Generated user-only packages are evaluated under their intended invocation policy. No repository-wide convention was edited.

**Reasoned qualification:** this is a reversible research scope, not a finding that the user's eventual use cannot need a native call-tool service. If such an interface is necessary, R4 must explicitly revise the product contract and budget before implementation. Calling the package generally portable today would be unjustified.

**Next step:** R4 chooses actual host/model versions, loader/interface, dependency and permission fixtures, and how registration/execution are verified. Compatibility tests belong to subsequent execution, not this source audit.

## C3. Source versions and admissibility

**Disposition: accepted and independently extended.** The version-specific record in [D1](source-register.md#d1-skillsbench) replaces the obsolete single-version picture. [D2](source-register.md#d2-swe-skills-bench) and [D3](source-register.md#d3-skilllearnbench) now identify precisely which inferences their accessible texts can support. The register contains an admission matrix for every source class.

**Change:** the main document no longer relies on a headline gain to establish its framework. All three direct preprints can be removed without invalidating the definitions, counterexamples, host distinction, or need to separate selection from confirmation. Newest, primary, and relevant do not mean replicated or sufficient for every claim.

**Additional finding:** the current benchmark's construction filtering deserves attention as well as its run filtering. Selecting for separation can be useful for diagnostic sensitivity, but it is not neutral sampling for deployment benefit. This is a transport limitation, not an accusation about intent. Raw attempt-level data and a population argument would be needed to evaluate the magnitude and direction of selection effects. Likewise, an interval for a marginal rate is not automatically an interval for a paired treatment contrast.

**Reasoned qualification:** do not discard all direct preprints because a repository is inaccessible or peer review is unestablished. Use the inspected paper for bounded reported observations; prohibit inaccessible implementation claims. The SWE ratio's sign/zero-denominator problem is demonstrated algebraically in D2, not inferred from a poor result. The final TMLR text remains excluded from inspected evidence; the accessible pinned preprint still supports its limited methodological use.

**Next step:** R4 may identify disclosed public development tasks. Any later attempt to use a study for power, expected effect, or native-creator ranking requires appropriate loading, data, selection, and variance verification. No such upgrade occurs here.

## C4. Fair attribution and probe integrity

**Disposition: accepted with narrower inference, tests deferred.** Independent inspection confirms the split, withheld improvement feedback, held-out selection, early termination, shared directory, own-name detector, text-keyed aggregation, and exception conversion. See [audit sections 2.1-2.4](implementation-audit.md#21-the-split-called-test-is-used-for-selection) for immutable anchors.

**Change:** the audit credits the authors' explicit validation-selection purpose. It does not imply hidden leakage, misconduct, or an unbiased-generalization claim absent from the inspected source. The numerical counterexample establishes the possibility of selection optimism, not its magnitude here. The statement that a new independent final set is the only possible valid route was corrected: justified nested or selection-aware inference is also possible.

The shared catalog supplies a static feasible interleaving, not a runtime result. R3 adds the critic's required instrument qualification table and also records the code's undefined-denominator reporting convention. Raw counts, delayed activation, technical errors, duplicate IDs, full-window traces, and actual package execution must remain distinguishable.

**Baseline fidelity:** leave the native pinned creator intact. A repaired probe that changes creation feedback defines an additional method; a common external evaluator can instead assess all frozen outputs. Do not quietly weaken the public baseline, omit expensive native steps selectively, or present a harness artifact as evidence that a new creator wins.

**Next step:** R4 specifies catalog-isolation/error-injection diagnostics and the external metric contract; R6 measures behavior after host/budget authorization. No effect frequency, score correction, or performance deficit is asserted now.

## C5. Skill and creator estimands

**Disposition: accepted and formalized; one dimensional ambiguity corrected.** Main section 3.1 includes solver/environment randomness and distinguishes a weighted finite suite from a transported population. Forced body injection, explicit loading instructions, and native invocation remain separate diagnostic interventions. Pairing resets initial conditions; it does not reveal two outcomes in the same live world.

Main section 11 defines the complete creator policy, generated artifact/status, production-quality estimand, and broader authoring-value estimand over a horizon. The critic's proposed per-episode utility minus horizon cost was potentially dimensionally ambiguous. R3 sums outcome utility over the same horizon as prospective costs and prohibits double counting. Where values are not commensurable, report vectors.

**Change:** unsuccessful/invalid/over-budget generations remain in the assigned-brief denominator. Production quality and routing quality are reported separately. Broader value uses a frozen fallback with failed-creation costs retained; appropriate reuse/no-new-skill decisions can be useful without hiding hard briefs. Human answers, all generation attempts, selection budgets, family weights, nested units, and native-system versus adapted-method comparisons are explicit.

**Information boundary:** freeze the creator before new evaluation-family briefs; freeze each artifact before downstream confirmation. The solver sees its legitimate task/input, never the hidden solutions/grader. The staged table describes access, not a nonexistent implemented control. A digest or separate conversation is insufficient enforcement.

**Next step:** R4 chooses the primary estimand, concrete statuses/fallback, brief distribution/weights, human-help policy, budget, host comparison, and independent custody or exploratory-only label. No claim of a sealed holdout is made.

## C6. Observability and evaluator calibration

**Disposition: accepted and revised.** Main section 2.3 supplies units, trace/oracle, a defeating counterexample, uncertainty, and permissible inference for each metric. Section 4 replaces observed understanding with observable loading/access/action events. Resource access and self-report do not prove causal reliance.

**Change:** evaluator repeatability on fixed outputs, substantive validity against independently checked fixtures, and repeated solver success are separate checks. Shared wrong oracles can produce agreement without truth. Critical false passes cannot be diluted by cosmetic agreement. Valid noncanonical CSV algorithms and appropriately delayed/substituted activation are concrete calibration cases. Ambiguous routing contexts remain in end-to-end evaluation and have disclosed coverage if excluded from binary routing ratios.

**Terminology correction:** the draft's discrimination question is sensitivity to meaningful change, not technical discriminant validity. The project is proposing validity arguments, not adopting a validated psychometric scale.

**Next step:** R4 creates the evaluator qualification plan, critical fixtures, adjudication policy, trace-completeness checks, and feasible human-review budget. The table is not evidence the grader has already passed.

## C7. Proportionate evaluation and prospective accounting

**Disposition: accepted and operationalized.** Main Stage F distinguishes development, bounded adoption, and comparative research. Permissions and severe constraints apply at every tier, but a reversible personal aid does not need a large confirmatory study merely to be useful.

**Change:** section 7 declares the decision perspective/horizon, sunk versus prospective costs, all-traffic catalog costs, variable eligible-use costs, human effort, and retirement. Creator-specific selection costs are charged; shared research infrastructure is reported separately. Costs are subtracted only in common defensible units and once.

The low-risk worked example includes an explicit hypothetical evaluation ceiling, break-even, forecast sensitivity, and a retain-the-script outcome. It never treats the ceiling as permission to skip minimum checks or as a real user's approved budget.

**Reasoned qualification:** one should stop evaluating when additional information cannot justify its cost, but not convert an economic ceiling into acceptance of severe risk. Reducing scope or keeping a safer incumbent is the fallback.

**Next step:** R4 obtains or clearly marks pending the actual budget, unit conversions, risk owner, likely usage, and practicality margins. It cannot invent an “industry-standard” threshold.

## C8. Missingness, uncertainty, and comparative decisions

**Disposition: accepted, conceptual rules settled; numerical design deferred.** Main Stages C-D now separate operational timeout/budget failure, verified external outage, ambiguous missingness, and invalid-oracle cases. Reruns preserve original attempts and spent resources. Report conditional healthy-infrastructure scores separately from the operational policy's success.

**Change:** the framework separates suite, solver, creator, task, and family uncertainty; preserves paired discordance; requires sensitivity to exclusions; and forbids exchanging more seeds for population coverage. Superiority, worthwhile advantage, noninferiority, and equivalence require different predeclared margins. Multiple-comparison adjustment does not erase adaptive choice of the problem, baseline, rubric, or stopping rule.

The original precision and zero-failure examples survive independent arithmetic checks; the assumptions and coverage limitations remain explicit. No universal sample count is proposed.

**Next step:** R4 writes the executable timeout/rerun tree, attempt schema, sampling/weighting/clustering plan, finite claim family, margin owner, pilot-variance plan, and stopping rule before R6 results. If few independent families or missing telemetry prevent credible inference, narrow the claim rather than manufacture precision.

## C9. Creator, package, execution, and grader threat boundaries

**Disposition: accepted and expanded.** Main section 6.4 specifies assets, attacker control, ingress, invariants, enforcement, residual risk, and benign/adversarial test pairs. Lower-trust embedded data cannot expand scope, but an authorized machine-readable request can carry instructions under its approved contract. Trust is about source and contract, not file format.

**Change:** coverage extends to authoring references, package scripts/dependencies, updates and name collisions, executor inputs, uncertain mutation retries, and grader injection. Provenance/version/scope and revision conditions prevent an unverified authoring guess from becoming an authoritative reusable rule. Controlled sinks and inert fixtures avoid requiring real secrets/destructive actions. Blanket refusal fails usefulness; clean final state does not erase transient leakage.

**Limit/next step:** R4 specifies a bounded threat model and enforceable instrumentation for the chosen hosts; R6 runs simulated checks and reports exactly what was observed. Zero incidents are not certification, and natural-language safeguards are not proof of enforcement.

## Decisions R3 settles and leaves open

**Settled for protocol design:** four quality predicates; host-loaded initial product; vector-first measurement; separate skill and creator-policy evaluation; failures included; two information boundaries; observable metrics; risk-proportionate tiers; prospective costs; qualified evidence; faithful baselines; noncompensating critical constraints.

**Still requires evidence:** native compatibility, source-loading fidelity, probe-interference frequency, grader sensitivity/validity, solver and creator variance, benefit of package components, maintenance burden, transport to intended users, and comparative outcomes.

**Still requires an owner/value choice:** intended families and prevalence; actual call interface if a service is needed; primary estimand; budget/horizon; adequacy and worthwhile-effect margins; severity policy; human-review access; and genuine holdout custody versus exploratory scope. R4 should propose concrete options and identify blockers rather than silently settle these from the literature.

The exact next prompt is in [HANDOFF.md](../HANDOFF.md). Verification and its limits are recorded in [verification-r3.md](verification-r3.md). R3 does not authorize R5 implementation, paid tests, a merge, or repository-security changes.
