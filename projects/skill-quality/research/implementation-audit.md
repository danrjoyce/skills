# Public implementation audit

Audit date: **2026-10-02**. This is a static source audit, not execution of the creators or a performance comparison. All observations refer to immutable commits below. Private or installed instruction variants are not reproduced or used as public evidence.

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

**What this does not imply:** it does not invalidate the development loop, imply intentional misrepresentation, or prove poor generalization. It means an independent final set is necessary before turning the selected score into a confirmatory claim. The creator's wording about avoiding overfitting should not be read as a guarantee of unbiased final performance.

### 2.2 The trigger probe measures an early routing decision

Exact source: [run_eval.py](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py), blob `e58c70bea39d5b252a1e819f242bbdcdf20e8b87`.

- [Lines 51-68](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L51-L68) create a temporary command containing the description and a minimal body, rather than installing and executing the complete candidate package.
- [Lines 128-178](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L128-L178) inspect early stream events. Several branches return after the first tool selection or message boundary. A different initial tool can produce `False` before a later legitimate invocation would occur.
- [Lines 221-234](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/scripts/run_eval.py#L221-L234) append `False` on a worker exception and threshold the trigger rate. In a negative case, that can contribute to an apparent pass.

**Inference:** this is a useful targeted early-trigger probe, not a complete measure of multi-turn discovery or downstream usefulness. For a confirmatory harness, separate technical error, observed abstention, delayed use, and successful execution. The actual frequency and practical effect of these code paths have not been measured.

### 2.3 Development convenience versus confirmatory discipline

The creator starts with a few cases and writes detailed assertions while runs are underway. The standard evaluation guide permits assertions after initial outputs. This helps discover what should be measured during development. Freeze primary criteria before an independent confirmation run; otherwise outcomes can influence the yardstick.

The [Agent Skills guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/skill-creation/evaluating-skills.mdx) recommends removing or replacing assertions that always pass in both configurations. Our narrower proposal is to distinguish a **discriminating effectiveness measure** from a **mandatory regression invariant**. A check that source files are preserved can remain essential even when both candidates currently pass it.

Likewise, subjective quality still needs evaluation. It may require anchored human comparison rather than mechanically countable assertions. “Hard to automate” does not mean “irrelevant to quality.”

## 3. Claims requiring independent critique

The next reviewer should verify the code anchors and challenge these inferences:

1. Is the distinction between development selection and final confirmation stated fairly?
2. Do the trigger probe's early exits materially differ from the intended discovery contract?
3. Are the validator discrepancies correctly interpreted without overclaiming about runtime behavior?
4. Are we fairly preserving the creators' strengths and platform-specific constraints?
5. Which proposed improvements would impose cost without enough evidential benefit?

An audit of code can expose risks and define tests. It cannot establish that a rewritten creator outperforms either baseline.
