# Critical Fact Verification (`critical-atomic-verification@1.1.0`)

Recovered name: Critical Atomic Verification

Purpose: Concentrate verification on the smallest facts whose failure would invalidate the output.

Activate when: small factual errors could change the outcome.

Do not use when: no factual conclusion or consequential action depends on the output; the content is purely expressive.

Requires: none.

## Runtime mechanism

Build a dependency graph from the intended conclusion back to minimal truth-bearing atoms. Mark an atom critical when its falsity, reversal, or absence would change the conclusion or safe action. Verify every critical atom directly at depth proportional to risk; propagate any failed or unknown atom forward so the dependent conclusion is repaired, qualified, or blocked.

## Procedure

1. State the conclusion or action being certified.
2. Decompose it into atomic claims and dependencies.
3. Use a removal or reversal test to mark critical atoms.
4. Assign verification depth and evidence requirements by consequence.
5. Verify each critical atom independently and record true, false, unknown, or conflicting.

## Guardrails

- Mandatory even on strong models: criticality test; atom-wise evidence status; uncertainty propagation.
- Conflict/precedence: A false critical atom vetoes any dependent conclusion; An unknown critical atom requires qualification or abstention, not a guessed value.
- Stop or fail when: Do not certify a conclusion while any indispensable atom is false, materially conflicting, or unsupported beyond the allowed risk threshold.

Full package and provenance: [`critical-atomic-verification`](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md).
