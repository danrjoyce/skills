# R9 independent readiness review

2026-10-02. Reviewed `08c73746c256fbed73910b13f09589b510e96231` in a fresh context. Scope: the frozen [v2 package](../../candidate/evidence-skill-creator-v2/SKILL.md), its [R8 report](../r8/README.md), [later assessment proposal](../r8/assessment-plan.md), and the [R7 critique](../r7/critique.md). This review inspected instructions and reran deterministic checks only. It did not execute a creator, generated helper, consumer, semantic reviewer, or native loading test.

## Decision

**Ready for a separately authorized limited assessment. No material package defect requires another revision.** V2 is an economical, usable general-purpose authoring workflow on inspection. Accept the frozen package for a bounded smoke test; do not call it empirically better, installed, or ready for general adoption. Another prose rewrite or larger evaluation framework is not the necessary next step.

The proposed two-family comparison is proportionate to the question of whether this creator deserves a supervised trial. Before launch, settle the few operational choices below, freeze the actual task bytes and checks, and obtain explicit authorization for the new live scope and evidence destinations. Those are launch conditions, not reasons to edit v2.

## Why the package passes this review

The four-step path is complete enough to follow without its former assessment machinery. It identifies the intervention, recovers a working contract, builds the smallest useful package, and checks a consumer's promised result. The 664-word entrypoint and 4,665-byte two-file package are verified size measurements, not quality scores. Optional scripts and references must earn their place; the runtime does not depend on research documents or an evaluator.

The central repair is logically appropriate. Creating an absent target in an authorized existing directory is different from replacing a file. V2 permits the former, requires replacement authority for the latter, and requires state inspection before retrying an uncertain mutation. It neither instructs deletion to satisfy a check nor treats every existing path as safe. Testing from the supported consumer state directly addresses R6's author-workspace mismatch. This establishes that the instructions address the diagnosed failure mechanism; it does not establish that agents will follow them.

Inspection against concrete counterexamples found no contradictory default:

- An export destination already exists but its targets do not: the contract allows authorized creation without a needless overwrite question.
- A target already contains unrelated content, or a link leads outside the allowed destination: authority and path checks remain necessary; the first-use instruction does not permit destructive repair.
- A service action has an uncertain result: inspect the actual state before retrying. If it cannot be established, authority or outcome remains unresolved rather than becoming presumed consent.
- A source-grounded draft already exists: inspect the existing package and affected callers, establish allowed edits, and preserve unrelated behavior. A text-only host can return reviewable instructions with saving and execution honestly unrun.
- A typo in an existing skill: the explicit focused-check exception avoids restarting a full workflow trial. A material behavior change gets the realistic use and relevant boundary instead.

These are reasoning checks, not observed passes. Path races, duplicate service effects, faithful draft preservation, and unnecessary clarification still require observation in a concrete host.

The essential evidence and safety boundaries survived simplification. Sources are required for uncertain or changing claims; examples and retrieved instructions supply data, not authority; executable dependencies need inspection; secrets and private instructions stay out of deliverables. Checks must distinguish passed, failed, and unrun, retain failures through revision, and bound adoption to tested conditions. Consequential workflows require stronger evidence and approved test scope, so one benign example is not offered as a universal safety qualification.

The description separates creation and revision from ordinary task execution and general skill questions. Name, folder, frontmatter and UI metadata agree. Model/user reach is consistent with the repository defaults. These are valid packaging and trigger-design observations; actual routing accuracy is untested. The [Agent Skills specification](https://agentskills.io/specification), [official OpenAI loading documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills), and [activation guide](https://agentskills.io/client-implementation/adding-skills-support#step-4-activate-skills) support the documented representation and loading routes. A file read can load instructions; metadata does not register an API/MCP function or grant tool access. No native compatibility claim follows.

## Settle three details before the smoke test

### 1. Fix state carryover and a fair direct control

The proposal correctly retains both the exact [concise template](../r6/simple-template.txt) and direct execution as serious alternatives. Freeze what each second use receives. New inputs alone do not define the starting state of a repeated workflow.

For the batch family, specify the authorized existing directory and exact absent targets, protected neighboring content, then changed input and an authorized second destination. For the draft family, use the actual first-use draft as the second-use starting artifact, with new source evidence and precisely bounded edits. If first use fails, keep that failure; use a separately identified common supplied draft for the second case or mark it blocked, according to a rule fixed beforehand. Do not silently repair it.

The direct control must receive the same task facts and intended workflow state. State whether useful helpers from its first use are retained. Retaining ordinary task artifacts and self-created helpers is a credible repeated-use control and does not require a creator-authored skill. If direct execution instead starts without them, label the result as comparison with repeated from-scratch execution, with that limitation. Keep the v2/template packages unchanged between uses and make their identity explicit. Equal host access and budgets do not establish equal backend model identity or isolation.

### 2. Define the small practical outcome before seeing results

Four author slots and eighteen consumer slots are correctly counted: one v2 and one template package per family; three policies, two families, and first/second/boundary uses. This gives twelve positive-artifact and six boundary opportunities, not eighteen interchangeable successes. All fixed slots, including missing packages, timeouts and unrun consumers, stay visible. Package production, selected version, author-report completion and budget observability remain separate.

Define a clarification/repair as a user or supervisor intervention needed to complete the supported positive task; report autonomous debugging separately in observed effort. Correct refusal in the boundary case is expected behavior, not a repair penalty. Judge output correctness, preservation and authority coverage separately. With only two second-use observations per policy, a zero-intervention tie is entirely plausible. Report no observed advantage in that case; do not add cases until one policy wins. A narrower user preference may still follow from a disclosed tradeoff, but neither amortized savings nor superiority is established.

The new briefs expand domain coverage. The directory/collision mechanism is already known, and cases authored by the same project team are development evidence. Fresh contexts and withheld final input text do not turn shared readable storage into independent holdout custody. Do not pool R6's ten cases into this denominator or present repeat benchmark results as unseen.

### 3. Treat time and evidence as real launch gates

At the proposed maxima, four eight-minute authors plus eighteen two-minute consumers consume **68 minutes**. With fifteen minutes of preparation, that leaves only **seven minutes** before the 90-minute experimental stop for admissions, transitions and interim recording. The additional thirty minutes protects final reconciliation/publication. The arithmetic fits, but a full 22-slot completion guarantee is unjustified.

Keep 22 as a ceiling. Before each admission, reserve its full allowance plus termination/recording time before minute 90; do not read the boundary as permission to start a final eight-minute run at minute 89. If overhead exhausts the margin, retain remaining assignments as unrun and report an incomplete assessment. If a strict complete 22-slot assessment is required, approve a revised schedule before launch rather than extending it in response to results. No new live work should begin while a prior stop is unconfirmed.

The available environment supports file inspection, local artifact retention and curated GitHub publication; those paths are exercised by this review. Complete action traces, authoritative global call counts, exact serving model and monetary usage are not established. Future records should retain the actual output-producing commands/scripts, attributed versus observed results, directory/state manifest and final bytes. Useful artifact-only conclusions remain possible with incomplete telemetry, but full authorized-action and cost claims do not. Before admitting live work, confirm its supported stop/terminal-status route and the exact permitted local/public evidence destinations. Do not launch a separate qualification campaign merely to expand this smoke test.

## Minimal next work and stopping condition

1. Keep v2 frozen. Finish one compact launch specification containing the two exact synthetic briefs, first/second/blocked states, source/output checks, state-carryover rule, fixed selection/missingness policy, order, intervention definition and feasible stopping rule. Use the existing proposal with the clarifications above; no new evaluation platform is needed.
2. Obtain approval for that bounded live comparison, its host, USD 0 new external spend, maximum four author/eighteen consumer slots and declared evidence retention/publication. An installation or native-discovery test would need separate authorization. If the evidence or stopping route cannot be supported, stop before admissions and name the blocker.
3. Run only that approved scope. A scoped trial recommendation needs useful first and second use in both families, appropriate boundary behavior and the declared practical gain over the simpler alternatives, with effort and missing evidence disclosed. Ties or cost tradeoffs support no preference or a user decision. A concrete failure may justify a separately versioned fix; the frozen tested package and all failed attempts remain intact.

R9 ends with this review. No live test was launched and no implementation correction is required by these static findings.

## Historical evidence remains unchanged

R6 remains closed: seventeen fresh admissions plus one same-author resume, four selected packages, one development solver, ten downstream cases, and 84 primary assignments gated/unrun. Its original 112-start, 616-minute, 1760-call, 250-MiB and USD 0 bounds, creator 15-minute/30-call and consumer four-minute/20-call limits, and 120-minute setup bound are unchanged. The approximately 32-second conservative setup-bound overshoot, unverified loading cap, 244-second semantic notification interval against 240, interrupted A0 reporting, and unknown actual active-time compliance remain in the [terminal-status correction](../r7/r6-status-addendum.md). No later assessment refunds that campaign's allowance. The three denied raw archives remain local and were neither read nor retransmitted in R9.

[Deterministic checks and publication verification](../verification-r9.md).
