# R8 verification

2026-10-02. Implementation and deterministic static checks only; no creator, downstream solver, generated helper or semantic-reviewer trial. No installation, promotion, merge or settings/protection change.

## Starting state and scope

Fresh remote ref resolved to `fbc7a59232c1d74c4928b385cd8b7e1a5d08613c`. Its complete untruncated tree was the source of the working materialization. Of 110 selected project/guidance blobs, 109 matched inherited local bytes; the R6 journal differed because its local copy included the later stop append. The exact remote journal was fetched instead. That original evidence is preserved, and the later facts remain in R7's addendum.

Authorized changes are the separate v2 package, new R8 research/verification files and three current project-tracking documents. Everything else, including v1 and all historical research/support/freezes, must remain byte-identical to the start commit. The denied archives are not in this materialization or publication set.

## Local checks

Run from the repository root, with already-installed Python/PyYAML/jsonschema:

```sh
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/r8/verify.py
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/r5/verify.py
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/verify-r4.py
```

- R8 format/freeze check: two regular UTF-8 files, folder/name agreement, nonempty description, UI metadata, model/user invocation defaults, prose convention and byte identity. Result: [static-results.json](r8/static-results.json). This narrow checker is outside the shipped candidate and does not execute it.
- V2: 664 entrypoint whitespace words; 4,665 package bytes; tree SHA-256 `cd74d8380c5aefbdc3ae4b8b77e2fd59a74323c5ecbb714a17a20e972afe53a9`. V1: 904 words, 22,273 bytes and the unchanged original tree identity. Counts measure size, not quality.
- R5's static checker passed: six v1 files, eleven frozen support files and fifteen protected original research files. It checks recorded-control consistency, not a new experimental qualification.
- The public OpenAI `quick_validate.py` at `49f948faa9258a0c61caceaf225e179651397431` passed on v2. Its local bytes and the public creator/reference identities were checked against the published R6 inventory. The validator only checks a limited frontmatter/naming profile; it does not establish native discovery or decisions. No validator code was copied into v2.
- Final R4 relative-link/schema/arithmetic check and complete changed-path preservation check are recorded with publication below. Existing protocol arithmetic is checked without restarting the protocol.

All behavioral and native-activation checks are **unrun by design** in R8. First-use and collision behavior are instructions awaiting observation. No full-action, cost, safety-rate or superiority claim follows from packaging passes. R6 timing and custody gaps remain in the [status correction](r7/r6-status-addendum.md).

## Setup observations and failures

The inherited `skills-r6` directory was not a Git checkout; an initial `git status` command exited 128. No mutation followed from that failed command. Source-backed files and the GitHub tree/commit interface were used for the authorized branch instead. An initial tracking patch was rejected for duplicate path operations before it applied; it was corrected, with no candidate changes. The OpenAI documentation Markdown endpoint returned an internal error; the official HTML page provided the required compatibility facts. None is a candidate behavior result. No failed candidate check was discarded or converted into a pass.

## Publication

Substantive R8 commit: `687608b851fd8a1f99d15d40d705223f33a9bfa0`. A fresh PR read confirmed that exact head, open and draft. All twelve intended changed files were independently fetched by commit and matched the local UTF-8 bytes exactly. The complete untruncated remote tree (391 entries) was compared with the starting tree: exactly those twelve project paths changed, comprising three current tracking documents and nine new v2/research files. All prior candidate, support, research evidence and every outside-project blob/mode remain unchanged; the denied archives remain absent.

The R4 static checker passed 278 relative links/anchors, schema and unchanged protocol arithmetic. R8 package/freeze checks and the R5 preservation check passed. These are deterministic checks, not a new qualification or live trial.

For this exact substantive commit, workflow-run, combined-status and check-run endpoints each returned zero records. The combined state was `pending` with zero statuses. This is absent CI, not running or passed CI.

A final tracking-only commit updates this verification record and the current handoff to record the observed publication. Its bytes, two-path delta, actual head and exact-commit CI are verified separately and reported in the PR status, avoiding a self-referential commit hash. No package, freeze or experiment is changed by that checkpoint.
