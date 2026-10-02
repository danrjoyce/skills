# R8: a smaller practical creator

2026-10-02. Implementation only, starting from `fbc7a59232c1d74c4928b385cd8b7e1a5d08613c`. [Use the two-file v2 package](../../candidate/evidence-skill-creator-v2/SKILL.md). Its entrypoint is 664 whitespace-delimited words, versus v1's 904. This is a reduction in reading and maintenance surface, not a measured improvement in decisions.

## What changed and why

The ordinary path now has four steps: choose the intervention, establish the working contract, build, and check first use. Material starting state is part of the contract alongside inputs, outputs, tools and authority. An authorized existing directory is distinguished from an occupied target. Actual collisions and uncertain mutations still require preservation or reconciliation, not destructive workarounds. Equivalent state is considered for non-file workflows without imposing directory rituals.

The package contains only `SKILL.md` and repository-required `agents/openai.yaml`. The assessment template, assessment/source references and inspector remain intact in v1 but are not dependencies of v2. No repeated runtime need justified carrying them forward. Existing public format validators can do packaging checks; research records belong here. This trades a built-in extended evaluation procedure for a shorter everyday authoring path. Consequential actions still need stronger checks and host permissions; comparisons still need declared alternatives and evidence.

The new instruction to check a realistic consumer start is a design response to the shared R6 integration failure. It is not a tested cure. R8 ran no creator, solver, generated helper or semantic reviewer. The package includes no experiment schema, case answers or method labels. [Static checks and limits](../verification-r8.md), [immutable v2 inventory](candidate-freeze.json).

## Calling and installation compatibility

The candidate remains outside shipped skill buckets and is not installed or promoted. This revision makes no plugin, router, configuration or permission changes. The existing router was read; advertising an uninstalled research package as a shipped choice would be misleading.

For a host that can read repository files, a review-use prompt can be:

> Read `projects/skill-quality/candidate/evidence-skill-creator-v2/SKILL.md` and use it to create a skill for [repeated workflow]. Inputs: [sources]. Starting state: [relevant state]. Output: [artifact and destination]. Allowed effects: [scope]. Target host/tools: [available capabilities].

Explicit file loading is a practical instruction-loading route, not evidence of automatic discovery or native tool registration. The supplied fields are an example, not a mandatory questionnaire; the creator recovers what is already known.

Current OpenAI documentation says Codex discovers local skills under repository `.agents/skills` and user `~/.agents/skills`; CLI/IDE invocation uses `$skill-name` or `/skills`, while ChatGPT selection uses `@`. After a separately authorized installation of this folder into a supported location, `$evidence-skill-creator-v2` is the intended Codex name. `agents/openai.yaml` provides UI metadata; omission of an explicit-only policy preserves model and user reach. These are documented mechanics, not a native-host test of this candidate. No installation was performed. [Official host documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).

A skill is not itself an API/MCP function. A host must discover and load its instructions, using file reading or an activation tool. Registering a function, supplying a service implementation, or adding persistent tool access is separate integration work. Metadata does not create that infrastructure or authorize effects. [Agent Skills integration guidance](https://agentskills.io/client-implementation/adding-skills-support#step-4-activate-skills).

## Response to R7 C1-C10

Dispositions concern this implementation. Historical missing evidence remains missing.

| Item | Disposition | Response and remaining limit |
| --- | --- | --- |
| C1: safe stop versus contract defect | Accepted | Step 2 distinguishes allowed new-file creation, occupied targets, unsafe paths and uncertain outcomes; step 4 checks the consumer's supported state. R6's legitimate conservative refusals and scores remain unchanged. Runtime improvement is untested. |
| C2: supervision and budgets | Partially accepted | [The later proposal](assessment-plan.md) reserves recording/publication headroom and narrows claims to observable artifacts. R6 counts, timing uncertainty and stop caveat remain in the [status correction](../r7/r6-status-addendum.md). No prose change verifies its historical caps or refunds budget. |
| C3: operational simplicity | Accepted | Four steps, two files, no mandatory ledger/status taxonomy/ownership ceremony or benchmark. Typo changes get focused checks. The 240-word reduction is descriptive; usefulness still needs observation. |
| C4: units, repeat use and alternatives | Accepted | R6 is one package per creator and two shared-state cases, not eight independent creator failures. Known cases remain development evidence. The later proposal retains a fixed template and direct solution, another workflow family, and real second use; no pooled or general superiority result. |
| C5: action history and publication | Partially accepted | Future minimum capture includes relevant initial state, commands/scripts, results and outputs, with authority coverage reported separately. All three denied archives stay local; no re-encoding or alternate channel. Complete action coverage and public raw custody cannot be restored in R8. |
| C6: A0 production versus reporting | Accepted | Separate package production, selection, author report and budget observability in the proposed record. The original A0 selection stands; missing report/final calls stay unknown. No replacement report or retroactive exclusion. |
| C7: source versus native fidelity | Accepted | R6 remains a constrained common-host adaptation. This candidate has documented loading routes but no native-runtime validation. The later minimal comparison uses v2/template/direct; it makes no new claim about public native creator systems. |
| C8: shared background capabilities | Accepted | The later proposal records host capabilities and observed loading by category without copying private instructions. Common background access, possible contamination and evaluation overhead remain limits; neither blindness nor actual contamination is inferred. |
| C9: semantic judge scope | Deferred | The four-public-control annotation check remains narrow and timing-limited. No new semantic grading was needed for static packaging. A later output needing judgment uses source-bound review with valid alternatives and explicit unresolved disagreements, not a general judge-reliability claim. |
| C10: current tracking and usable outcome | Accepted | v2, this response, freeze/checks, current navigation and the [next fresh-context task](continuation.md) are supplied. Publication verification checks exact paths, bytes and commit CI. Missing CI is absence, not success. |

## Public basis and claim scope

- [R7's critique](../r7/critique.md) and frozen R6 artifacts support the specific state/authority distinction. They do not establish that v2 is better.
- [Pinned public OpenAI creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md) supports concise, task-specific packaging and optional resources. Its [validator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py) is a limited format check, not a behavioral test. Public source identities were rechecked locally against the retained inventory. No source code is copied into v2.
- [Agent Skills specification](https://agentskills.io/specification) supplies the folder/frontmatter contract; the integration guide above assigns activation to the host. Official mechanics are authority about format and loading, not effectiveness evidence.
- Repository [invocation conventions](../../../../.agents/invocation.md), [research](../../../../skills/engineering/research/SKILL.md) and [writing-for-agents](../../../../skills/productivity/writing-for-agents/SKILL.md) informed repository fit. The explicit sequential-task constraint overrides background delegation here. This artifact is original synthesis of public material and project findings; private installed instructions/prompts were not copied or published.

Official web mechanics were checked on 2026-10-02. The older OpenAI URL redirected to ChatGPT Learn; its Markdown endpoint failed, so the readable HTML supplied the cited mechanics. A source-access failure is not evidence against the skill. There is no new literature-based performance claim in R8.
