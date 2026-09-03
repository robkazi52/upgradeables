# Structural System Edit (`surgery-edit@1.1.0`)

Recovered name: Surgery Editing

Purpose: Make macro changes to layers, cores, workflows, or incompatible interfaces without losing invariants, dependents, or rollback control.

Activate when: layers, Cores, or workflows require major replacement.

Do not use when: a localized invariant-preserving patch suffices; the replacement architecture lacks acceptance criteria.

Requires: none.

## Runtime mechanism

Declare the failing structural boundary and why CRISPR cannot preserve it, inventory every inbound and outbound interface, and define a replacement architecture with mapped invariants. Plan old-to-new state migration, adapters, staged cutover, observability, and rollback; change the structure in bounded phases, validate each dependent contract, then remove the old path only after the replacement passes global checks.

## Procedure

1. Document the architecture-level failure and evidence that local editing is insufficient.
2. Inventory components, state, public and internal interfaces, dependents, precedence rules, and invariants.
3. Design the replacement structure and map every old responsibility and interface to retain, adapt, retire, or explicitly reject.
4. Define migration order, compatibility adapters, checkpoints, observability, rollback, and cutover criteria.
5. Implement or specify the replacement in stages while validating each interface and state transfer.

## Guardrails

- Mandatory even on strong models: CRISPR-insufficiency proof; interface inventory; old-to-new mapping.
- Conflict/precedence: Use CRISPR when all required behavior can coexist with current interfaces inside a bounded patch; A hard invariant without a valid old-to-new mapping blocks cutover.
- Stop or fail when: macro edit disguised as patch accumulation; unmapped dependents.

Full package and provenance: [`surgery-edit`](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md).
