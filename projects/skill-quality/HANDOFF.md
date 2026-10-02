# Research handoff

Updated: **2026-10-02 UTC**.

## Current state

R1 has produced a substantive foundations draft and supporting research records. Publication and remote verification are the remaining R1 steps at this checkpoint. The branch is `research/skill-quality`; the review is [draft PR #1](https://github.com/danrjoyce/skills/pull/1), based on main at `3cca18b368ae95cdbdebbff572ccafa662551015`.

The project is research documentation only. No final meta-skill, performance benchmark, sealed holdout, or superiority result exists. No merge or bulk upstream synchronization is authorized by this checkpoint. Repository protection is a separate concern and is not established by this research.

## Artifacts

1. [Main analysis](how-to-determine-if-a-skill-is-good.md)
2. [Source register](research/source-register.md)
3. [Pinned implementation audit](research/implementation-audit.md)
4. [Source-version manifest](research/implementation-pins.json)
5. [Methodology and limitations](research/methodology.md)
6. [Task ledger](TASKS.md)

## Durable findings and uncertainty

- The draft defines quality relationally and evaluates marginal usefulness, not just artifact appearance.
- Activation, execution, and whole-deployment effects need different tests.
- Public creator code is evidence of implementation behavior, not empirical superiority.
- The source audit identifies selection/test and trigger-measurement distinctions that require independent verification.
- The three direct 2026 benchmark papers use different task-selection and execution conditions. They are provisional evidence, not interchangeable estimates.
- No target task distribution, resource budget, release threshold, independent holdout boundary, or calibrated grader has been finalized.

Do not treat these findings as instructions to agree with the draft. The next task is to try to falsify its claims and improve the argument.

## Exact fresh-context prompt for the next substantive task

```text
Work on R2 only in GitHub repository danrjoyce/skills, branch research/skill-quality, draft PR #1. Inspect the current branch and repository guidance before any write. Read AGENTS.md and CLAUDE.md, then projects/skill-quality/README.md, TASKS.md, HANDOFF.md, how-to-determine-if-a-skill-is-good.md, and the supporting research files. Use the source artifacts and publicly linked primary evidence rather than relying on the prior author's private reasoning.

Independently critique the first research draft. Determine whether its definition of a good skill is coherent, useful, sufficiently complete, and operationalizable. Verify consequential source claims and code anchors. Challenge its causal estimands, activation labels, sample and holdout logic, generalization claims, safety treatment, cost accounting, and distinction between evaluating a skill and evaluating a creator. Look for counterexamples, excessive process, missing strong sources, unsupported thresholds, and unjustified transfers from other fields. Treat the OpenAI and Anthropic baselines fairly and do not infer misconduct from methodological limitations.

Write projects/skill-quality/research/critique-01.md with an overall verdict, prioritized specific issues, file/section/source anchors, counterexamples or evidence, concrete revisions, claims that survive scrutiny, and unresolved questions. Separate factual errors, contested value choices, methodological weaknesses, and optional improvements. A useful negative finding is welcome. Do not edit the main analysis yet and do not implement the final meta-skill. Update TASKS.md and HANDOFF.md with the completed critique and a precise revision prompt, then publish the critique on the same draft PR without merging.

Keep one substantive task active at a time. Do not start parallel research workers or bulk-sync upstream. Do not copy private or internal instruction text or unrelated personal information into the public repository. Renew context conservatively around 50,000 to 60,000 tokens and before approximately 90,000; stop earlier at a coherent checkpoint. Return the critique artifact and commit, the most important corrections, verification limits, and the exact next task.
```

## If R1 publication was interrupted

First compare local or pending research content with the actual remote branch and PR. Finish remote byte and changed-path verification before marking R1 complete. Do not recreate the branch or duplicate the PR. Record the verified substantive commit in the ledger. Then proceed with the fresh-context critique as a new task, not by extending the original author's context.
