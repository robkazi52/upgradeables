# Bounded Change Rules (`controlled-drift-corridors@1.1.0`)

Recovered name: Controlled Drift Corridors

Purpose: Enable adaptation, compression, or creativity without surrendering semantic control.

Activate when: synthesis or creativity must coexist with fidelity.

Do not use when: all content is zero-drift; allowed dimensions cannot be tested.

Requires: none.

## Runtime mechanism

Partition the artifact into regions or claim types and assign each a corridor specifying fixed invariants, allowed dimensions of change, maximum semantic distance, evidence requirements, and rollback trigger. Transform only after the corridor is explicit, then compare output to the source and tighten or revert any region outside bounds.

## Procedure

1. Segment the task into regions with materially different tolerance.
2. For each region, list invariants and allowed changes such as tone, length, order, or abstraction.
3. Set validation metrics or review questions and a rollback threshold.
4. Transform one region inside its corridor.
5. Compare claims, obligations, entities, and required structure to source.

## Guardrails

- Mandatory even on strong models: explicit allowed dimensions; locked invariants; region-specific validation.
- Conflict/precedence: Higher-authority task constraints and zero-drift fields override corridor permissions; If validation signals disagree, apply the narrowest supported corridor or request review.
- Stop or fail when: Stop transformation when invariants cannot be measured or recovered; Revert regions that cross the boundary instead of rationalizing post hoc.

Full package and provenance: [`controlled-drift-corridors`](../../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md).
