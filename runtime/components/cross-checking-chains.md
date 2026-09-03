# Cross-Checking Chains (`cross-checking-chains@1.1.0`)

Purpose: Make validation ordered, traceable, and resistant to repeated correlated checking.

Activate when: a conclusion relies on a dependency chain.

Do not use when: one direct authoritative check fully resolves a low-risk atom; checks cannot be ordered by dependency.

Requires: none.

## Runtime mechanism

Design a chain whose links have distinct jobs—such as identity/provenance, extraction, entailment, independent corroboration, and consequence testing. Each link receives the claim plus the prior evidence ledger, may add evidence or a typed failure, and cannot erase an upstream failure; certification requires every mandatory link to pass or an explicit resolution branch to close the discrepancy.

## Procedure

1. Select the critical claim or atom.
2. Enumerate its verification dependencies in causal order.
3. Assign each link a distinct evidence source or validation lens.
4. Define required input, pass condition, and typed failure for every link.
5. Run links in order and preserve the accumulating ledger.

## Guardrails

- Mandatory even on strong models: dependency order; link independence; failure propagation.
- Conflict/precedence: Prerequisite failure blocks dependent links from certifying the claim; A disagreement between independent links requires explicit resolution, not majority counting.
- Stop or fail when: Do not certify when a mandatory link fails, is skipped, or depends on the same untested assumption as its supposed corroborator.

Full package and provenance: [`cross-checking-chains`](../../upgradeables/validation/cross-checking-chains/UPGRADEABLE.md).
