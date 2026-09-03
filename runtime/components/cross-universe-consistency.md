# Alternative-Scenario Consistency Check (`cross-universe-consistency@1.1.0`)

Recovered name: Cross-Universe Consistency Mode

Purpose: Prevent a final synthesis from combining mutually exclusive premises harvested from different candidate worlds.

Activate when: parallel candidate paths are compared.

Do not use when: only one branch was explored; branches are explicitly independent deliverables and will not be collapsed.

Requires: none.

## Runtime mechanism

Represent each candidate universe as assumptions, invariants, derived claims, and chosen actions. Compare same-named claims across branches, label invariant conclusions versus branch-conditional conclusions, detect premise incompatibilities, and permit the final collapse to import an element only with the assumption set that makes it valid.

## Procedure

1. Record assumptions, constraints, claims, and actions for every branch.
2. Align comparable claims across branches.
3. Mark claims invariant, compatible, conflicting, or incomparable.
4. Trace each proposed final element back to its branch assumptions.
5. Reject combinations whose assumptions cannot coexist.

## Guardrails

- Mandatory even on strong models: assumption provenance and compatibility check for any hybrid.
- Conflict/precedence: A branch-conditional claim cannot be imported without its enabling assumptions; A decisive safety contradiction survives branch collapse even if other branches omit it.
- Stop or fail when: Block the collapse when it combines mutually exclusive assumptions or strips a claim from conditions required for its validity.

Full package and provenance: [`cross-universe-consistency`](../../upgradeables/validation/cross-universe-consistency/UPGRADEABLE.md).
