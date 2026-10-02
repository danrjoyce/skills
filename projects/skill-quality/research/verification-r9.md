# R9 verification

2026-10-02. Independent document/package inspection and deterministic checks only. [Review and decision](r9/review.md). No creator, consumer, generated helper, semantic reviewer or native-loading trial was run. No package was modified, installed or promoted.

## Input identity and scope

A fresh branch read and PR read both confirmed `08c73746c256fbed73910b13f09589b510e96231`, with PR #1 open and draft. The complete untruncated starting tree has 391 entries. The PR's complete 116-path change list is confined to `projects/skill-quality/`. All 121 files in the selected local materialization matched their remote Git blob identities before review edits. Root repository guidance, invocation conventions and relevant research/writing guidance were read; `AGENTS.md` points to `CLAUDE.md`.

R9 changes only three current tracking documents and three new review/check records. Both candidate packages, R1-R8 nontracking evidence, freezes, support, repository configuration and outside-project files must remain byte-identical to the reviewed commit. The denied raw archives were not opened or included in the working/publication set.

## Deterministic checks

The inspected R8 checker recomputes package inventory and SHA-256 identity and checks name/frontmatter, UI metadata and invocation defaults. It passed on the frozen candidate: two regular files, 664 entrypoint whitespace words, 4,665 total bytes, tree SHA-256 `cd74d8380c5aefbdc3ae4b8b77e2fd59a74323c5ecbb714a17a20e972afe53a9`. The v1 tree remains `4dc5eef71128fcb98b2ab27c6163a91fc701c91854a8ba3df9dafa9965b55683`.

The R5 deterministic preservation checker passed for six v1 files, eleven support files and fifteen protected original artifacts. Its recorded-control consistency check is not a new qualification. The R4 document/schema/arithmetic checker passed 278 relative links/anchors before review edits; its final link count is in [static-results.json](r9/static-results.json). Historical protocol arithmetic was checked without reopening the protocol.

The pinned public OpenAI `quick_validate.py` source was read and its Git blob identity rechecked against a fresh read at `49f948faa9258a0c61caceaf225e179651397431` before execution. This is a limited format validator, not a host-discovery or behavioral test. All checks use existing local dependencies; no installation or API spending occurred.

Reproduction from a repository materialization, with existing Python/PyYAML/jsonschema:

```sh
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/r8/verify.py
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/r5/verify.py
PYTHONDONTWRITEBYTECODE=1 python projects/skill-quality/research/verify-r4.py
```

Run the public validator separately only from the inspected pinned source. Its success concerns the supplied metadata profile. Current Agent Skills format and OpenAI loading documentation were checked as primary sources and linked in the review. No public or private creator instructions were copied into the deliverable.

The package's boundary and non-file examples were inspected logically. Their behavior is **unrun**. Runtime enforcement, native activation, model/cost equality, complete action history, and comparative usefulness remain unestablished. The available file and GitHub tools demonstrate a supported route for curated review artifacts, not complete experimental trace capture. Future live work remains subject to a settled stopping/evidence contract and explicit new authorization.

## Observed limitations and publication

The inherited materialization has no Git checkout metadata; an initial status/log probe returned exit 128. Review uses remote tree/blob identities and the GitHub tree/commit interface instead. Large combined read results were truncated; relevant documents, code and metadata were reread in bounded calls. Neither observation is a candidate failure.

Substantive R9 commit: `27f1f17db3dd8cb7bf9e3f9739e5901e13ab8aa8`. All six changed files were independently fetched at that exact commit and matched the intended UTF-8 bytes. Its complete untruncated tree has 395 entries; comparison with the reviewed starting tree found exactly the six intended paths: three current tracking documents, the new review, static results and this verification record. All prior package, research/support/freeze and outside-project blob identities and modes remain unchanged. The PR read confirmed that exact head, open and draft.

The final R4 check passed 295 relative links/anchors and unchanged schema/protocol arithmetic. R8/v1 preservation and the inspected pinned public validator passed. No behavioral checks were added. For the exact substantive commit, workflow-run, combined-status and check-run endpoints each returned zero records. Combined state was `pending` with zero statuses: absent CI, not running or passed CI.

A tracking-only checkpoint records these observed checks in this file and HANDOFF. Its two-path delta, exact bytes, actual head and exact-commit CI are verified separately in the final PR status, avoiding a self-referential commit hash. That checkpoint changes no candidate, experiment, historical evidence or finding.
