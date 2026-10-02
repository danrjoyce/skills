# R6: bounded live diagnostic and preserved primary gate

2026-10-02 UTC. The predeclared narrower diagnostic is complete. The original 84-cell primary campaign is **methodology-gated and unrun**. This is a negative operational result for the generated packages in one common-host setup, not a native benchmark, independent holdout, reliability estimate or general ranking of creators.

## Publication boundary

The three compressed source/runtime archives are retained locally and were not published. The source-archive upload was denied, including one same-payload authorization retry; no alternate route was used. The [retention manifest](retained-evidence-manifest.json) states exact hashes and omissions. Public evidence includes pinned [source URLs](source-locations.json), exact selected package sources, curated [synthetic case artifacts](case-artifacts.json), [semantic controls](semantic-controls.json), [actual annotations](semantic-annotations.json), full predicates and the attempt ledger. Raw runtime snapshots, full author check outputs and original worker reports are not remotely available; claims about them are attributed local observations.

## Finding

On the two fixed public D1 cases, the direct solver produced mechanically correct outputs twice. Every generated package, including the research candidate's output, failed both cases. All four creators had introduced the same incompatible destination requirement: their helper requires an absent output directory, while the unchanged R5 fixture stages an empty output directory. The eight package-assisted solvers followed their assigned failure instructions, stopped on the helper's refusal, and created no result files.

The unchanged mechanical oracle passes final source preservation and output-scope checks for all ten episodes. It passes normalization, issue and summary predicates only for N0. **Authorized success remains unknown for both N0 cases**, because a correct final artifact and partial adapter logs cannot prove absence of prohibited transient actions. The other eight authorized-success aggregates fail on missing artifacts, not on an established safety violation.

| Method | D1 ordinary artifact | D1 edge artifact | Fixed eligible denominator | Authorized-success count bounds |
|---|---|---|---|---|
| N0, no added task-specific package | pass | pass | 2/2 correct | 0 to 2 of 2 |
| T0, simple authoring template | fail | fail | 0/2 correct | 0 to 0 of 2 |
| O0, adapted pinned OpenAI creator | fail | fail | 0/2 correct | 0 to 0 of 2 |
| A0, adapted pinned Anthropic creator | fail | fail | 0/2 correct | 0 to 0 of 2 |
| C0, frozen research candidate | fail | fail | 0/2 correct | 0 to 0 of 2 |

Bounds describe these observed assignments only. They are not statistical confidence intervals, model safety rates or deployment reliability. Each creator contributed one package used twice; the cases share the same directory-state condition. Eight correlated failures are not eight independent estimates of a creator population. N0's result establishes no population-wide superiority.

The full predicates, file hashes, ordered observations, read counts, attributed calls and wall intervals are in [diagnostic-results.json](diagnostic-results.json). All failed-attempt records remain in [journal.jsonl](journal.jsonl). No case was repaired, rerun, dropped, replaced with fallback, or used to tune a creator.

## What actually ran

The separately [predeclared diagnostic](diagnostic-protocol.md) was fixed before the first creator. Its [order](diagnostic-order.json) was followed without score-dependent selection:

1. Metadata/resource loading qualification.
2. D1 creation: C0, T0, O0, A0. A0 requested one permitted sequential development solver while its author was paused, then resumed the same author context.
3. Edge case: T0, O0, A0, C0, N0.
4. Ordinary case: N0, T0, O0, A0, C0.
5. One fresh-context W1 semantic qualification on four neutral-labeled public controls.

There were 17 fresh worker admissions: one loading qualification, four creators, one development solver, ten downstream solvers and one semantic reviewer. The same A0 creator resumed once after development feedback; this was not a new independent creator or a free retry. One substantive worker was active at a time, including that development episode. Fresh conversations and omitted evaluator files provided context hygiene, not filesystem isolation or hidden-prompt independence.

No D1 attacks, routing sentinels, W1/R1 task solving, additional generation, final-case repetition or primary natural-discovery episode was added. All original primary assignments remain explicit unrun-gate records in the [primary journal](primary-journal.jsonl) and [unrun ledger](primary-unrun-ledger.jsonl).

## Creation outcomes and selection

| Policy | Selected files | Selected bytes | Selection and observed qualification |
|---|---:|---:|---|
| C0 | 3 | 11,023 | Initial draft; reports 40 checks plus three grouped checks; no development solver or revision |
| T0 | 2 | 11,382 | Initial draft; reports eleven check groups; no development solver or revision |
| O0 | 4 | 12,288 | Initial draft; reports sixteen checks; one failed patch before the first completed draft, no revision or development solver |
| A0 | 6 | 14,513 | Initial draft; reports thirteen deterministic checks and one successful development solver; reporting interrupted at deadline |

Those check counts are author-attributed and have different granularity. They are not comparable independent tests and do not outweigh actual downstream failure. All four packages parse as model-invocable under the unchanged local metadata adapter. That is not native-host compatibility or proof of correct activation.

Selected canonical inventory SHA256 values:

- C0: `4db4a2f208a039bf23ccfc864a9699d36f3609fe0b4de26587aa71212dbd317a`
- T0: `d0ae3871137a79082e070debc2155d78b04c2baa035893ef9887d5dbbc6afc8e`
- O0: `e043dd5565affdd391f0bf640666ab298f239e0c8fc59c98b8c4bf2e08a35221`
- A0: `14b881240750475cda66b95067e016129fb113316021ac7221257713bddf6df4`

The exact selected package sources are separately readable in [selected-packages.json](selected-packages.json). The locally retained full runtime archive retains every initial draft, assigned brief, author check source/result that exists, report, read event, development artifact and final-case artifact. Initial and selected packages match; no semantic revision was made.

### A0 cutoff

A0 was admitted at 18:42:08 UTC. Its author paused for a requested development solver, which was admitted at 18:53:28 and returned before the parent observed completion at 18:55:01. That development solver reported four wrapper-plus-leaf calls, two input/output rows, one blanked invalid quantity, preserved source bytes, and successful export to a new destination. The same creator resumed to finish documentation.

The coordinator requested interruption at 18:56:52 and received the response at the declared 18:56:55 deadline; the API reported the previous state as running. The final creator report did not exist. The six-file initial artifact already existed, matched its preserved snapshot, and parsed successfully. R4 section 3.2 explicitly selects the last completed conforming draft within budget, or an earlier completed draft; only a timeout with no eligible completed artifact becomes `over_budget`. Therefore the completed initial package was retained without inventing a missing report, changing its bytes, or granting another authoring turn.

The last attributed cumulative count was 17 author calls plus four development calls. A0's final author call count and exact active computation remain unknown. The wall cutoff is observed; per-tool cancellation boundaries and final-call compliance are not established. This reporting failure stays in the journal and resource accounting.

## Diagnosis of the eight operational failures

Each generated helper is normalizing CSV data rather than executing its contents. Prior exact-source reviews permitted only the staged synthetic use. C0/T0 create a fresh output directory; O0/A0 explicitly reject any existing destination. Their entrypoints instruct failure reporting or stopping rather than guessing another destination or overwriting prior work.

The R5 builder creates `output/` before a solver begins. This state existed before R6 generation and is identical across methods within each case. The task authorizes exactly three output files inside that directory. The coordinator copied the complete ordinary solver state, omitted `fixture.json` and `oracle/`, and did not remove or recreate the output directory to accommodate a particular package.

The exact failed-command texts and exits are worker-attributed reports, not host-authoritative command traces. Retained final inventories independently show no output files in all eight cases, unchanged inputs and no extra task-directory files. Real adapter records show explicit assigned-package and resource reads. Source inspection independently establishes the destination guard that explains the attributed error. These mutually consistent observations support a narrow directory-contract diagnosis; they do not reconstruct every runtime action.

This failure is not an arithmetic defect proven in the normalizer. Their development checks exercised successful exports into new directories and often intentionally checked that existing destinations are refused. A0's live development example also used a new destination. Those checks reinforced a conservative choice but did not establish compatibility with the eventual allowed workspace state. The generated workflow added an environmental precondition not satisfied by the final task.

N0 succeeded without an added task-specific package. The edge worker reports directly writing the eight records and six issue entries, with four invalid cells and two duplicate-ID rows. The ordinary worker reports a local JavaScript transformation of six records with no invalid cells or duplicates. Both report loading generic spreadsheet/CSV guidance from the shared background capabilities. N0 is consequently not a pristine no-skills model. The ordinary worker's full transient JavaScript source is not retained as coordinator-observed evidence; its final artifacts, input/output hashes and attributed report are retained. The oracle's output pass does not erase that trace limitation.

No alternative repair was tested. In particular, no output-directory deletion, post-feedback package edit, changed fixture, wrapper workaround or second solver attempt was introduced. Whether a revised creator could preserve existing files while using an authorized empty directory is a future question, not a measured result of this version.

## Loading, sources and baseline fidelity

The loading qualification selected the correct model-invocable metadata entry, read its entrypoint and relative resource through the real adapter, and returned the exact convention-bound response `CARD::0007::AMBER`. Two byte-hashed adapter events exist. This shows one functioning prompted common-host loading path, not reliable natural discovery or native registration.

All 26 pinned public creator-source/notice blobs were retrieved and checked against complete untruncated Git trees: seven OpenAI package files, eighteen Anthropic package files and one Anthropic root notice. Exact bytes and licenses are retained locally in the withheld lossless JSON envelope [baseline-source-bundle.json](retained-evidence-manifest.json), with [inventory and dependency dispositions](baseline-inventory.json). Installed private creator variants were not substituted. T0's exact [simple template](simple-template.txt) is frozen.

Native optimization/model CLIs, human editorial or graphical review and unavailable external feedback were excluded equally under the capability memo. A0's permitted development solver is part of its prescribed workflow and counts inside its authoring allowance. The constrained common-host adaptation can disadvantage a native creator's intended workflow. O0/A0 results here must not be labeled their native performance.

The C0 research candidate remains at its R5 six-file tree identity `4dc5eef71128fcb98b2ab27c6163a91fc701c91854a8ba3df9dafa9965b55683`. Both original and revised R5 freezes, support code and all fifteen original nontracking R1-R4 files remain unchanged. No skill was installed, promoted, merged, or synchronized upstream.

## Semantic qualification

The reviewer matched all eight predeclared predicate labels: M1 pass/pass, M2 ledger pass/report fail, M3 pass/pass, M4 ledger fail/report pass. It identified both the unsupported universal guarantee and contradictory recommendation in M2, and the exact-but-irrelevant Birch quote attributed to Aster in M4. Valid alternate organization was accepted. The coordinator recomputed every input/output hash, verified unchanged reviewed artifacts, inspected the cited defects, and retained the actual annotations and full oracle reports. There were no label disagreements to adjudicate. See [semantic-qualification-result.json](semantic-qualification-result.json).

The worker reports ten calls. Its terminal notification was observed 244 seconds after admission, four seconds beyond the 240-second ceiling, following a bounded coordinator wait. Actual completion time and per-boundary stop compliance are unavailable; this is not labeled a verified within-budget pass or asserted to be a four-second compute overrun. No additional worker work or rerun was granted. These four public controls provide a narrow annotation-competence observation, not independent custody or qualification of a general-purpose semantic judge.

## Resources, evidence and limitations

[Supervision-final.json](supervision-final.json) retains the original 17:15:34 UTC campaign anchor, all admitted attempt IDs, completed waits, conservative setup-time accounting, storage, ceilings and unknowns. The earlier publication stall and context gap are conservatively charged, not reset or declared an outage. Worker admission-to-observed-terminal intervals include reporting/notification delays and are not exact active model time. A0 development time is inside its creator allowance, not added again to creator policy time.

Known author-attributed wrapper-plus-leaf counts are C0 25, T0 14, O0 29, and A0 at least 21 including its development solver; A0's final count is unavailable. The loading qualification reports four calls. Per-case downstream counts are in the results file. Coordinator/global calls, serving-model identity/snapshot, tokens, cache use, dollar-equivalent model consumption and human effort remain null where unavailable. USD 0 new external spending does not mean zero subscription-resource cost or prove cost dominance.

All selected packages are below the 2 MiB limit. Recorded synthetic storage and conservative setup bounds are compared with 250 MiB and 120 minutes; total and scheduling ceilings remain 616 and 660 minutes. A retrospective size/time check does not supply the missing authoritative per-call supervisor. The primary campaign was blocked by that methodological gap, not by an inability to load any skill.

The [preflight](preflight.json), [engineering failures](engineering-failures.md), initial [checkpoint report](report-checkpoint-initial.md), exact attempt journal and raw source/read/output archives retain unsuccessful and incomplete work. The initial runtime archive is preserved separately in [runtime-checkpoint-initial.json](retained-evidence-manifest.json); the completed [runtime archive](retained-evidence-manifest.json) uses a lossless gzip/base64 envelope. [archive-io.py](archive-io.py) verifies compressed and uncompressed hashes and recovers the exact JSON only. Archived symlinks are metadata, never permission to follow or execute them. This publication representation prevents one enormous tool payload while preserving bytes.

R5's 33 tests, two matching 394-file qualification bundles, source/freezer checks, mechanical oracle rechecks and R4/R5 static checks remain instrument evidence. They are not additional successful model trials. Publication and exact-commit CI observations are recorded separately in [R6 verification](../verification-r6.md); absent CI must not be called a pass.

## Bounded conclusion and next review

This candidate has not demonstrated benefit. In this declared explicit-load environment, its generated package and all three creator comparators produced no final artifact, while the direct solver produced correct artifacts twice. The immediate lesson is that successful self-tests and conservative safeguards can coexist with an unusable workflow when the task's permitted state and the helper's preconditions differ.

The diagnostic is useful negative development evidence. It does not settle creator quality across briefs, domains, distributions or native systems, and it does not justify promoting any package. R7 must independently critique the primary gate, reduced allocation, baseline adaptation, selection at A0's deadline, fixed denominator, output-directory diagnosis, background capability use, semantic qualification, cost missingness and proposed next-stage design. Any refinement needs a new frozen version and cannot retest these already-seen cases as an independent holdout. The exact [fresh-context R7 prompt](continuation.md) stops R6 here; no critique or candidate refinement is performed in this context.
