# Source Note — Temporal Anchor Scaffold

- Slug: `temporal-anchor-scaffold`
- ID: `JAN26-07`
- Source support: `source-gap`
- Mechanism basis: `provisional`
- Final status: `BLOCKED_BY_SOURCE_GAP`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `GLOBAL_LOCAL_ANCHOR_SPLIT_T1` (historical_assistant_artifact)

## Recovered or normalized purpose

Prevent chronology errors and confusion between event time, publication time, and current validity.

## Operational mechanism

A modern interpretation is a task-local table of events with normalized timestamp or interval, original temporal expression, source, event/publication/effective-time type, confidence, and before/after links. Unknown order stays unknown. Promote only durable verified temporal facts into canonical state and retire the scaffold after the timeline-dependent output is validated.

## Trigger and task use

Triggers: time or chronology affects correctness. Best-fit tasks: incident timelines, policy version analysis, case chronology, news or market research.

## Interactions and failure boundary

Companions: state-snapshot, sequential-memory-state-engine, micro-scaffolding. Failure boundary: Do not assert total order from partial temporal evidence.; Treat the mechanism as provisional until original concept-specific documentation is recovered..

## Unresolved details / interpretation boundary

Only the label and neighboring temporal architecture are recovered. The table-and-retirement mechanism is a conservative modern interpretation, not claimed history.
