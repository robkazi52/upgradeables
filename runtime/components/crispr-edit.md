# Precision Local System Edit (`crispr-edit@1.1.0`)

Recovered name: CRISPR Editing

Purpose: Make high-confidence micro-edits to structured systems without collateral semantic or interface drift.

Activate when: a change is small and local.

Do not use when: the governing structure is wrong; multiple interfaces must be redesigned.

Requires: none.

## Runtime mechanism

Construct a patch contract before editing: exact target coordinates, requested semantic delta, protected invariants, allowed collateral region, and validation probes. Snapshot the target plus its immediate dependency boundary, apply the smallest diff that realizes the delta, and compare before/after behavior on both the changed case and invariant cases. A patch that requires broad remapping is rejected and escalated to Surgery rather than stretched into disguised rewrite.

## Procedure

1. Identify the exact editable unit and the request's semantic delta.
2. Enumerate invariants: facts, IDs, interfaces, precedence, citations, unaffected behaviors, and formatting contracts that must not change.
3. Trace immediate inbound and outbound dependencies to set a finite collateral boundary.
4. Create and apply the smallest patch inside that boundary.
5. Run a positive probe for the new behavior and negative probes for each protected invariant.

## Guardrails

- Mandatory even on strong models: explicit invariant set; bounded dependency inspection; positive and negative probes.
- Conflict/precedence: Locked safety, truth, and authorization invariants cannot be included in the requested delta; If the new behavior and protected invariants cannot coexist, stop and expose the conflict.
- Stop or fail when: collateral semantic drift; syntactically valid but behaviorally wrong patch.

Full package and provenance: [`crispr-edit`](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md).
