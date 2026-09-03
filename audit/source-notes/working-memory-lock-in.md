# Source Note — Working-Memory Lock-In

- Slug: `working-memory-lock-in`
- ID: `T2-08`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Interpretation rule for the frozen T2 registry (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. Working-Memory Lock-In Heartbeats (historical_assistant_artifact)

## Recovered or normalized purpose

Prevent critical goals, constraints, identifiers, or safety conditions from being displaced by incoming context.

## Operational mechanism

Select only the invariants whose omission would materially corrupt the task, store canonical pointers plus compact current values, and run a heartbeat before major actions to confirm freshness and consistency. Refresh on accepted state change; if a locked item conflicts or goes stale, block dependent work until reconciled.

## Trigger and task use

Triggers: critical state competes with large context. Best-fit tasks: long agent loops, high-fidelity transformations, safety-critical execution, multi-step builds.

## Interactions and failure boundary

Companions: stateblock, task-set-lock-in, working-memory-cues. Failure boundary: Do not proceed when a critical locked field cannot be reconciled.; Shrink the set when lock overhead begins to reduce task performance..

## Unresolved details / interpretation boundary

Catalog and inventory recover the lock-in concept; the addendum's heartbeat and fidelity patterns support refresh, conflict, and release semantics.
