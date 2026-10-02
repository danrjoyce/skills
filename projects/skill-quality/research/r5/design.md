# Candidate design and requirement traceability

R5 produces an uninstalled research artifact, [evidence-skill-creator](../../candidate/evidence-skill-creator/SKILL.md). It is a standard host-loaded, model-invocable instruction package. Six files occupy 22,273 bytes. Only the 6,818-byte entrypoint is required up front; references, template and inspector are conditional. Bytes are not token counts. Nothing registers a native function, installs a plugin or changes the repository's shipped-skill/router catalog.

## Evidence and design status

The authoring workflow is a synthesis of the revised [measurement framework](../../how-to-determine-if-a-skill-is-good.md) and [R3 response ledger](../revision-01.md), repository invocation conventions, and these pinned public interfaces:

- [Agent Skills specification](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx): package layout and metadata. Its authority concerns the declared format, not behavioral effectiveness.
- [Public OpenAI creator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/SKILL.md): compact entrypoint, conditional resources and helper validation. The [pinned quick validator](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.system/skill-creator/scripts/quick_validate.py) was independently retrieved, inspected and run locally. Its blob `0547b4041a5f58fa19892079a114a1df98286406` matched the existing pin.
- [Public Anthropic creator](https://github.com/anthropics/skills/blob/8a1541c4a3ffa5a20a5a91de0dcf3f0bab1d1ef4/skills/skill-creator/SKILL.md): development/evaluation loops and output assessment motivate hypotheses, bounded by the [static implementation audit](../implementation-audit.md). No native loop was executed or repaired.
- [Agent Skills host integration guide](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/client-implementation/adding-skills-support.mdx): discovery, reading and execution require host support. A package alone cannot supply it.

These are public source references, not copied private installed instructions. Candidate prose and helper code are newly authored. Existing repository licensing applies; [source pins](../implementation-pins.json) remain unchanged. Complete baseline directories, transitive local references and license notices still require R6 materialization before any comparative trial. Selected-file pins are not a full source closure.

## Requirements, components and falsifiers

| Requirement | Smallest included component | Available check and falsifier | Current limit |
|---|---|---|---|
| Make a reusable skill only when useful; honor an explicit prototype | Entrypoint intervention choice and six output dispositions | Routing controls cover incumbent reuse, undecided policy and outside-scope requests; R6 must observe actual choices | No measured routing reliability |
| Recover known requirements and ask only material questions | Contract section | Inspect generated assumptions, permission boundaries and focused questions on a real authoring run | No model authoring run |
| Define outcome and risk before optimizing | Entrypoint plus conditional assessment reference | A check without observable predicates, safe evidence or valid alternatives would falsify conformance | Evaluation cost proportionality is proposed, not empirically optimal |
| Preserve source/version/authority and uncertainty | Conditional evidence reference | Trace a changing/conflicting claim to a source, scoped rule and revisit condition | No universal truth detector |
| Minimize runtime context and reusable components | Six-file package; optional template stays outside generated runtime package | Inventory, local links, name/description and actual component-use review | Byte size alone does not measure cognitive load or value |
| Distinguish format, behavior, adoption and comparative gain | Assessment reference and delivery contract | Misstating static validity as runtime success or dropping a failed creation invalidates the report | No fitness/adoption/superiority result yet |
| Keep trust and side effects within authorization | Entrypoint source trust, inspected scripts, host permissions and uncertain-outcome handling | Inert injection, transient violation and retry controls; actual trace needed later | Instructions and fixture paths do not enforce security |
| Capture costs, failed attempts and retirement conditions | Delivery/lifecycle paragraph and optional assessment template | Trace records, observed versus unavailable counters, rollback/revisit conditions | No complete runtime telemetry established |
| Catch simple packaging defects without executing package code | Read-only standard-library inspector | Missing/escaping links, symlinks, empty metadata and multiline-parser control | Limited scalar/link profile, not full YAML/Markdown or security certification |

The R4 numeric margins and pilot case answers are absent from the candidate. It does not embed source packets, task-family output schemas, the slugify repair, graders, baseline instructions or comparison budgets. Those belong to evaluator-side support. The optional inspector's generic boundary fix is disclosed in [amendment 2](amendment-02.md); the five instruction/reference/template/metadata files retain their original hashes.

## What was deliberately left out

No automatic model runner, description optimizer, native skill installer, universal score, arbitrary web scraper, evaluation-answer reference, unbounded interview or mandatory multi-worker ritual. The research support is larger than the creator because it records a falsifiable comparison; none of it is an operative creator dependency.

An ordinary host can read the package explicitly for a future diagnostic. Native implicit discovery, resource loading and call semantics remain untested. R6 must either qualify a common-host discovery path or label explicit-only loading as a diagnostic and leave the primary natural-activation claim unsupported. A generic model API with no loader/executor is an unsupported integration.

## Criticism that remains live

The workflow may be too cautious, too generic, more expensive than a template or no better than ordinary model behavior. Source triage and assessment references may be ignored. Permissive alternative dispositions could mask weak generation. The description may activate too broadly. Conversely, strict packaging checks may reject valid syntax outside their small profile; that is an incomplete/manual-review result, not a universal format verdict.

The comparison therefore retains N0 and T0, charges all failures and probes, separates routing and production, preserves unknown safety outcomes and permits a loss or null result. Tests of the helper/control code cannot settle these criticisms. Keep the candidate frozen through R6; any outcome-driven change belongs to a separately declared R7 revision and new evaluation stage.
