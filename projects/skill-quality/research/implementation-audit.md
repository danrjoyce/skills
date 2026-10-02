# Public implementation audit

Audit/revision date: **2026-10-02 UTC**, R3. All ten files in the revised manifest were independently fetched; blob identifiers matched. This is a static source audit, not execution of the creators or a performance comparison. All observations refer to immutable commits below. Private or installed instruction variants are not reproduced or used as public evidence.

## 1. OpenAI: useful construction guidance, narrow validation

Baseline: [OpenAI creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md), repository commit `49f948faa9258a0c61caceaf225e179651397431`.

**Verified observations:** the creator organizes work around concrete use cases, reusable scripts/references/assets, initialization, editing, validation, and iteration. It advises limiting unnecessary context and matching prescription to task fragility. These are useful authoring hypotheses, and script execution tests are explicitly encouraged.

The [validator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py#L15-L94) checks presence, YAML structure, selected keys, types, naming patterns, and description constraints. It does not run a downstream task or compare with a no-skill baseline.

Two precise compatibility caveats:

- The allowed-key set at lines 39-40 omits `compatibility`, which the [pinned Agent Skills specification](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx) permits. Therefore, a valid specification field can fail this particular validator.
- The checks at lines 59-76 and 81-89 are conditional on the stripped strings being nonempty. By static inspection, empty string values pass those branches, although the specification requires nonempty name and description. The validator also does not compare the name with the directory name.

**Inference:** “passes this validator” and “conforms fully to the current format specification” are different claims. Neither implies effective behavior. This is not a claim that actual deployed runtimes accept the same invalid inputs. Runtime parsing and other validation layers were not tested.

**Fair use as a baseline:** preserve the exact public version, including its intended workflow and resource tools. Do not silently substitute a different installed creator, improve its instructions only in one arm, or describe a minimal linter comparison as a comparison of complete creators.

## 2. Anthropic: a substantial development loop

Baseline: [Anthropic creator](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/SKILL.md), repository commit `8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4`.

**Verified strengths:** the workflow includes skill/no-skill or old-version baselines, realistic prompts, artifact and transcript inspection, time/token capture, quantitative checks, qualitative human review, and iteration. The [grader](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/agents/grader.md) is instructed to critique weak assertions and inspect actual outputs. The [comparator](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/agents/comparator.md) hides which skill produced each output.

These are substantive advantages over judging only prose or format. They still require valid sampling, clean baselines, calibrated grading, and a separate confirmatory evaluation for a superiority claim.

### 2.1 The split called “test” is used for selection

Exact source: [run_loop.py](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py), blob `30a263d674ef19de11c756d6f7537f91a421909e`.

Verified code path:

1. [Lines 24-44](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L24-L44): split queries, stratified by intended triggering.
2. [Lines 86-119](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L86-L119): evaluate both partitions at each iteration.
3. [Lines 194-208](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L194-L208): remove test-prefixed history fields before asking the improvement model for another description. This is a meaningful leakage precaution.
4. [Lines 216-234](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L216-L234): choose the best iteration by test-passed count when that split exists and return its score.

**Methodological inference:** the split is a validation/selection set for the final chosen description. Hiding its examples and scores from the improvement model does not make the final maximum an untouched estimate: the selection operator uses them. The size of any optimism depends on noise, candidate dependence, and the search. It is not measured here. [Cawley and Talbot](https://jmlr.org/papers/v11/cawley10a.html) explain the general selection problem.

**Purpose attribution:** [SKILL.md lines 375-404](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/SKILL.md#L375-L404) explicitly describes selection on the held-out score. This is ordinary validation selection meant to reduce overfitting to training feedback. No inspected passage claims that its selected maximum is an unbiased estimate of future performance. The implementation should receive credit for withholding selection feedback from the improvement prompt.

**What this does not imply:** it does not invalidate the development loop, allege hidden leakage/misconduct, or prove poor generalization. Independent confirmation is a simple way to support the additional generalization claim; a justified nested or selection-aware design is another. R1's wording that an independent final set is strictly necessary was too categorical.

**Algebraic illustration:** with two equally capable candidates of true success probability 0.5, and independent single binary selection observations, the expected selected maximum is `1-(1-0.5)^2=0.75`; selected true ability remains 0.5. This demonstrates a possible mechanism, not bias measured in this optimizer. Correlated scores, few candidates, or deterministic outcomes can change or eliminate this particular optimism. The [training-pass stop at lines 177-181](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L177-L181) can end the loop early; do not assume exactly five candidates.

### 2.2 The trigger probe measures an early routing decision

Exact source: [run_eval.py](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py), blob `e58c70bea39d5b252a1e819f242bbdcdf20e8b87`.

- [Lines 51-68](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L51-L68) create a temporary command containing the description and a minimal body, rather than installing and executing the complete candidate package.
- [Lines 128-178](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L128-L178) inspect early stream events. Several branches return after the first tool selection or message boundary. A different initial tool can produce `False` before a later legitimate invocation would occur.
- [Lines 221-234](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L221-L234) append `False` on a worker exception and threshold the trigger rate. In a negative case, that can contribute to an apparent pass.

**Inference:** this is a useful targeted early-trigger probe, not a complete measure of multi-turn discovery or downstream usefulness. For a confirmatory harness, separate technical error, observed abstention, delayed use, and successful execution. The actual frequency and practical effect of these code paths have not been measured.

### 2.3 Static shared-catalog risk and aggregation contract

[run_eval.py lines 51-89](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L51-L89) write a unique command name for each probe into one project `.claude/commands` directory and start the CLI in that root. [Lines 198-211](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L198-L211) submit concurrent probes with the same root. [Lines 128-168](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L128-L168) only recognize the probe's own generated identifier. Unique filenames prevent overwriting, not shared-catalog interference.

**Static counterexample:** A and B each write a command with the same description. If a CLI snapshot includes both, B could select A; B's name detector would return false. A probe can also remove its file while another is using the shared catalog. This is a feasible path conditional on CLI discovery behavior, not a reproduced incident. We did not test the CLI, discovery timing, existing installed skill, frequency, or direction/magnitude of scoring changes. Treating the baseline as empirically broken would exceed the evidence.

Additional verified instrument details:

- [Lines 213-242](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L213-L242) group by query text; duplicate texts merge runs and overwrite the label entry according to completion order. [run_loop.py lines 102-105](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L102-L105) partition returned records by membership in training query text. A duplicate spanning both splits can therefore be attributed to training. Supplied cases were not shown to contain such duplicates.
- The standalone CLI [defaults](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L259-L268) are ten workers, three repeats, threshold 0.5. Raw trigger counts are returned as well as thresholded query pass. Majority correctness under three independent identical-risk trials is `3p^2-2p^3`; at `p=0.9`, it is `0.972`, not 0.9. Independence is an illustrative assumption, particularly questionable with catalog interference.
- [run_loop.py lines 164-166](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_loop.py#L164-L166) print precision/recall as 1.0 for zero denominators. This is a reporting convention, not evidence of perfect selectivity. An external evaluator should retain undefined ratios and counts.

### 2.4 Instrument qualification plan, not completed tests

| Question | Required evidence before confirmatory use | Fairness constraint |
|---|---|---|
| Does parallel catalog overlap change decisions? | Frozen CLI/model, catalog snapshots, installed-skill inventory, randomized matched single-worker/shared-worker/isolated-worker probes, raw events and wall-clock | Keep native workflow unchanged as one arm; isolated mode is a labeled diagnostic, not a silent replacement |
| Can errors appear as correct negative cases? | Inject deterministic worker/CLI failures in inert harness fixtures and retain error status | Do not selectively remove failures from one creator |
| Is delayed activation valid? | Cases that require an initial inspection then appropriate skill loading; full-window trace and outcome checks | Distinguish early routing from deployment usefulness |
| Are duplicate cases handled? | Preflight unique IDs, duplicate-text/label consistency checks, explicit grouping across splits | Apply the same case policy to all arms |
| What does a reported rate mean? | Raw per-attempt activation/error counts, threshold settings, query-level majority scores, undefined denominators | Do not compare majority pass to another arm's single-attempt probability |
| Is full skill value measured? | Package digest, resource access/execution, downstream artifact and authorization checks | A minimal-description probe is not the complete creator or complete generated skill |

These requirements belong in R4's instrument plan and R6 execution after an appropriate environment/budget exists. Paid model calls, upstream edits, and diagnostic execution are not performed in R3. If only a common external evaluator can be qualified, it can grade every creator's frozen output while their native creation policies remain visible. If a repair changes what feedback the creator sees, that repair is a different creation method and requires a separate comparison.

### 2.5 Development convenience versus confirmatory discipline

The creator starts with a few cases and writes detailed assertions while runs are underway. The standard evaluation guide permits assertions after initial outputs. This helps discover what should be measured during development. Freeze primary criteria before an independent confirmation run; otherwise outcomes can influence the yardstick.

The [Agent Skills guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/skill-creation/evaluating-skills.mdx) recommends removing or replacing assertions that always pass in both configurations. Our narrower proposal is to distinguish a **discriminating effectiveness measure** from a **mandatory regression invariant**. A check that source files are preserved can remain essential even when both candidates currently pass it.

Likewise, subjective quality still needs evaluation. It may require anchored human comparison rather than mechanically countable assertions. “Hard to automate” does not mean “irrelevant to quality.”

## 3. Runtime contracts and residual evidence limits

The newly pinned [Agent Skills integration guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/client-implementation/adding-skills-support.mdx#L234-L280) distinguishes file-read activation, host-registered activation tools, and explicit user activation. The host, not `SKILL.md` alone, supplies that interface. Optional subagent execution is an integration choice. No runtime compatibility result follows from the guide or these hashes.

R2's C4 is accepted as a static instrument concern; R3 rejects stronger interpretations that validation selection is concealed leakage, an independent final set is the only possible valid inference method, or catalog overlap has a known practical effect. These stronger claims are not findings of the critic either. This distinction prevents the revised project from turning review language into a strawman.

Open empirical questions remain: native-host behavior; prevalence of probe errors/interference; downstream benefit of full workflows; equivalence of adapters; costs of repair and evaluation; and any comparative gain from a new creator. A source audit can define those tests, not answer them.
