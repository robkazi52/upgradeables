# Source Note — SelfBlock Auto-Update

- Slug: `selfblock-auto-update`
- ID: `T2-11`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — SelfBlock Auto-Update (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.1 Kernel / State Block (historical_assistant_artifact)

## Recovered or normalized purpose

Reduce stale state and forgotten deltas during iterative work.

## Operational mechanism

Attach an update hook to defined events, compute the smallest state delta, validate it against schema and authority, then atomically merge it into the live SelfBlock while retaining provenance or a change note. The updater may change status and observations but not silently rewrite locked goals, permissions, or immutable evidence.

## Trigger and task use

Triggers: the host can update explicit state after steps. Best-fit tasks: agent loops, long editing sessions, tool-rich workflows, multi-step investigations.

## Interactions and failure boundary

Companions: stateblock, working-memory-lock-in, state-snapshot. Failure boundary: Disable automatic writes when atomicity, schema validation, or authority checks are unavailable.; Escalate ambiguous changes to task identity or permissions..

## Unresolved details / interpretation boundary

The catalog directly recovers the auto-update behavior; atomic delta, authority, and version checks are a conservative operational normalization.
