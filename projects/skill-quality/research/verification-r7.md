# R7 verification

2026-10-02. This stage independently reviews retained evidence and publishes critique/status only. No candidate, generated helper, creator, solver or semantic reviewer was executed as a new trial.

## Starting state

Remote draft PR #1 was freshly read at `0e66e7eff6899f9e3082cbe9d67c3e9847966b1e`, parent `7833edd1edb6dc038fa30cbb90bf1ec4ac5f5ad2`. Its body was stale R5 text. The complete untruncated remote tree contains 102 project blobs. Local bytes matched 101; the sole mismatch is the R6 journal's later local stop append. That journal will not be changed in this publication. The later stop facts are summarized separately in [the status correction](r7/r6-status-addendum.md).

## Checks performed

- R5 static checker: six candidate files, eleven support files and fifteen original nontracking artifacts match the original inventories; candidate tree remains `4dc5eef71128fcb98b2ab27c6163a91fc701c91854a8ba3df9dafa9965b55683`.
- Fresh complete Git trees for the two public baseline pins matched all 26 archived source/license/notice blobs, each checked against byte length, SHA-256 and Git blob SHA.
- The accessible full local runtime envelope decoded with matching compressed/uncompressed hashes. All 450 file payloads among 652 entries matched their lengths/hashes. No symlink was followed and no archived helper executed.
- All four exact selected packages match both initial and current package files. Seventeen distinct worker starts have terminal records; all 84 primary terminal records remain unrun-gate. The ten recorded downstream cells match the fixed order.
- The existing public mechanical replay reproduced all ten reports from curated artifacts. This is static rescoring of retained bytes, not another model trial, independent execution or complete safety verification.
- Critique C1-C10, status addendum and the next implementation prompt are review artifacts. All unpublished archives remain excluded; no denied payload is retried.

Detailed observations and timing limits: [evidence-review.json](r7/evidence-review.json). The frozen R6 checker uses an earlier resource snapshot and is not a final cap certificate.

## Publication

Substantive R7 commit: `60bfad2a3661f89f68904e5f045b52f5403d7837`. A fresh PR read confirmed this exact branch head and the draft state. All eight changed files were independently fetched by commit and matched their local UTF-8 bytes exactly. A complete untruncated tree comparison against the R6 tracking commit found exactly the eight intended project paths: the three current tracking documents, this verification record and four new R7 review files. All original candidate/support/research evidence and every outside-project blob remain unchanged; the denied archives remain absent.

The final R4 static checker passed 246 relative links/anchors and retained protocol arithmetic. The R5 static freeze checker passed again after writing the review. These checks did not run a model or a generated helper.

For this exact substantive R7 commit, the GitHub workflow, combined-status and check-run endpoints each returned zero records. The combined state was `pending` with zero statuses, not evidence of running CI. This is absent CI, not a CI pass. A final tracking-only commit updates this verification file; its remote bytes/head and exact-commit CI are checked separately and recorded in the PR status. There is no further experiment in R7.
