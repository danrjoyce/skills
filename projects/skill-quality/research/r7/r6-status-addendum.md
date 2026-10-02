# R6 terminal status, corrected during R7

2026-10-02. This addendum preserves the published R6 records and records later stop evidence. It does not resume the experiment, reset a budget, change a score, or certify unseen actions.

## Publication and stop

The R6 substantive commit is `7833edd1edb6dc038fa30cbb90bf1ec4ac5f5ad2`. Its tracking child is `0e66e7eff6899f9e3082cbe9d67c3e9847966b1e`. At 20:04 UTC, a fresh PR read confirmed the tracking child as the actual head of draft PR #1. The previous immediate read had been stale. No ref update was retried. The PR body was still the older R5 status, so R7 replaces it once after reconciling the actual state.

The R6 worker's local stop record, recorded at 20:03:26 UTC, states:

- The conservative setup-time upper bound reached 120 minutes at approximately 20:01:43 UTC.
- The final publication cell was terminated at 20:02:15 UTC, approximately 32 seconds later.
- Exact active coordinator computation and global tool-call compliance are unknown. Do not report verified setup-cap compliance or assert that actual computation exceeded the cap by 32 seconds.
- All experimental workers were already terminal. Seventeen fresh admissions and one same-author resume remain the final experimental count. No trials, repairs, fallback or free rerun were added.
- The ref-update call had returned success; tracking-head confirmation and PR metadata update were uncertain at termination. R7's later read resolves the head uncertainty but does not invent a completed metadata write.

This review inspected that local record and the matching append to the local journal. The remote R6 journal is intentionally left unchanged; its bytes predate the append. This prose addendum communicates the material facts without sending any withheld archive payload. The [published supervision snapshot](../r6/supervision-final.json) is from 20:00:37 UTC and is not the final stop observation.

## Other resource unknowns

The loading qualification's journal `running` record is 17:21:19.154292 and its terminal bookkeeping record is 17:25:04.308875 UTC, 225.154583 seconds apart. Its declared limit is 120 seconds. Actual worker admission/completion timing is absent, so the record cannot verify cap compliance or establish a computation overrun. The successful exact response and two hashed adapter reads are separate valid observations.

The semantic review's admission-to-observed-notification interval is 244 seconds against a 240-second ceiling. Actual completion and boundary enforcement remain unknown. A0's package was retained under the original completed-draft selection rule, while report completion and final calls remain unknown. No later review can convert these missing fields into measured passes.

USD 0 new external spend is retained; it does not mean no subscription-resource consumption. Exact model, tokens, cache use, global calls and monetary consumption remain unknown. R7 is a separate document-review task after the concluded experimental campaign; it does not refund or reopen the R6 allowance.

## Evidence and CI boundary

R6's three compressed source/runtime archives remain local after the recorded authorization denial. No alternate upload route is authorized or attempted. Published curated outputs, selected packages, source locators and hashes remain the public evidence. R7 independently inspected accessible local bytes, which does not remove the public reproducibility gap.

The R6 stop record reports zero workflow runs, statuses and check runs for both R6 publication commits. R7 checks exact-commit CI for its own publication separately. Missing CI is not a pass. Current branch status and the unchanged primary gate are recorded in [HANDOFF](../../HANDOFF.md) and the [R7 critique](critique.md).
