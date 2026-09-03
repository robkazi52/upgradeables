# Downstream Invariant Protection (`drift-immunity-propagation@1.1.0`)

Recovered name: Drift Immunity Propagation

Purpose: Preserve established drift resistance across pipelines rather than only at the original source boundary.

Activate when: many downstream modules consume locked decisions.

Do not use when: no downstream artifact derives from protected material; protection metadata cannot accompany data and downstream validation is impossible.

Requires: none.

## Runtime mechanism

Represent each verified invariant with an identifier, source/provenance, scope, permitted transformations, and validation predicate. When producing a derived artifact or state projection, copy the applicable invariant contract and lineage pointer, require the receiver to acknowledge it, and test the derivative before it can become an upstream source for another stage.

## Procedure

1. Identify verified invariants and assign stable identifiers.
2. Define the derivation scope and validation predicate for each.
3. Attach applicable invariant contracts to every downstream projection or artifact.
4. Require receiving components to preserve or explicitly reject unsupported contracts.
5. Validate each derivative before further propagation.

## Guardrails

- Mandatory even on strong models: stable invariant identity; lineage; boundary tests.
- Conflict/precedence: Original verified source and higher-authority constraints outrank downstream paraphrases; If two inherited invariant contracts conflict, stop derivation and resolve lineage/authority before merging.
- Stop or fail when: Do not label a derivative immune when its invariant cannot be tested; Stop propagation across a component that cannot preserve required provenance or semantics.

Full package and provenance: [`drift-immunity-propagation`](../../upgradeables/drift-control/drift-immunity-propagation/UPGRADEABLE.md).
