# Source Note — Sequential Memory State Engine (SMSE)

- Slug: `sequential-memory-state-engine`
- ID: `T2-10`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.1 SMSE — Sequential Memory State Engine (historical_assistant_artifact)

## Recovered or normalized purpose

Preserve sequence, provenance, relevance, and current truth across long-running work.

## Operational mechanism

For each event, preserve source and time, normalize it into the state schema, classify affected fields, compare with the current version, resolve contradiction by authority and recency rules, commit an atomic delta, derive consumer-specific projections, and emit a checkpoint. History remains available, but only the resolved current state drives action.

## Trigger and task use

Triggers: state changes across steps or source chunks. Best-fit tasks: long-lived agents, case management, iterative research, multi-source evolving records.

## Interactions and failure boundary

Companions: stateblock, selfblock-auto-update, state-snapshot. Failure boundary: Stop dependent actions when a safety-critical contradiction cannot be resolved.; Do not assert chronological correctness when timestamps or event identity are missing..

## Unresolved details / interpretation boundary

The addendum supplies a detailed recovery of the staged engine, consistent with the catalog and historical family records.
