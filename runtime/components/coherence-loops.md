# Coherence Loops (`coherence-loops@1.1.0`)

Purpose: Repair cross-part inconsistencies while preventing endless self-review.

Activate when: local edits risk global inconsistency.

Do not use when: the discrepancy is isolated and a single deterministic correction suffices; no stable acceptance criteria exist.

Requires: none.

## Runtime mechanism

Freeze the governing invariants, locate the smallest inconsistent dependency set, repair the highest-leverage cause, and rerun checks across affected boundaries. Continue only while measured inconsistency decreases; stop on verified convergence, a fixed iteration/depth budget, repeated unchanged failure, or a conflict requiring external authority.

## Procedure

1. Record the detected inconsistency and governing invariants.
2. Trace affected dependencies and identify the earliest causal mismatch.
3. Choose the smallest repair expected to restore the widest agreement.
4. Apply or propose the repair and rerun local plus boundary checks.
5. Compare residual inconsistency with the prior iteration.

## Guardrails

- Mandatory even on strong models: explicit invariants, dependency recheck, and bounded exit.
- Conflict/precedence: Explicit invariants outrank local convenience; If repairs oscillate between two states, stop and expose the underlying unresolved tradeoff.
- Stop or fail when: Stop without certification when inconsistency does not decrease, repairs oscillate, or resolution requires changing a locked invariant.

Full package and provenance: [`coherence-loops`](../../upgradeables/validation/coherence-loops/UPGRADEABLE.md).
