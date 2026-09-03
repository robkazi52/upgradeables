# Source Note — Zero-Drift Zones

- Slug: `zero-drift-zones`
- ID: `T3-14`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — Zero-drift (historical_assistant_artifact)

## Recovered or normalized purpose

Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift.

## Operational mechanism

Identify minimal semantic atoms whose alteration would invalidate the task, assign stable IDs and source spans, and specify their preservation rule: exact text, exact value/unit, or meaning-equivalent statement with required qualifiers. Carry the IDs through all transforms and require a deterministic check or source-grounded review before acceptance.

## Trigger and task use

Triggers: content contains fidelity-locked atoms. Best-fit tasks: legal and policy transformation, source-grounded summaries, code/API migration, safety-critical instructions.

## Interactions and failure boundary

Companions: controlled-drift-corridors, drift-immunity-propagation, drift-suppression. Failure boundary: Block release when a required zone fails validation.; Do not claim semantic equivalence where domain expertise or source context is insufficient..

## Unresolved details / interpretation boundary

The catalog directly recovers zero-drift behavior, and the addendum supplies an explicit fidelity workflow and width mapping.
