# Skill quality research

Status: R1 foundations complete; independent critique is next. Started 2026-10-02. No skill-performance experiment has been run.

## Purpose

Determine what makes an AI-usable skill good, then develop and test a general skill-creation skill. The final aim is demonstrable improvement over strong public alternatives on declared task distributions, not an untestable claim of universal superiority.

This is a research project, not an installed skill. It does not change existing skills, plugin manifests, repository configuration, or upstream synchronization.

## Research contract

- Work on one substantive task at a time.
- Distinguish verified source claims, reasoned synthesis, proposed decision rules, and measured results.
- Prefer primary sources; evaluate empirical evidence separately from implementation authority.
- Pin implementations and preserve source anchors and uncertainty.
- Require fresh-context criticism and revision before implementing the final meta-skill.
- Keep evaluation data and holdouts separate from creation and tuning.
- Renew context conservatively around 50,000 to 60,000 tokens and always before the requested approximately 90,000-token ceiling. Checkpoint earlier at a coherent stopping point.
- Publish incremental work on a research branch and draft pull request. Do not merge.

## Navigation

- [How to determine if a skill is good](how-to-determine-if-a-skill-is-good.md): the substantive first analysis
- [Source register](research/source-register.md): evidence quality, claim scope, and limitations
- [Implementation audit](research/implementation-audit.md): exact public-code observations and methodological critique
- [Implementation pins](research/implementation-pins.json): machine-readable commit and blob identifiers
- [Methodology](research/methodology.md): search approach, verification, and unresolved questions
- [R1 verification record](research/verification-r1.md): publication checks and their limits
- [TASKS.md](TASKS.md): sequential task ledger and acceptance criteria
- [HANDOFF.md](HANDOFF.md): current state and exact restart prompt

The draft proposes a measurement and decision framework. It does not claim that a new creator has been built or has beaten any alternative.
