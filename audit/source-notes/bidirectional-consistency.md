# Source Note — Bidirectional Consistency

- Slug: `bidirectional-consistency`
- ID: `T2-18`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-18. Bidirectional Consistency (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — T2-18. Bidirectional Consistency (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.6 Global verification (historical_assistant_artifact)

## Recovered or normalized purpose

Expose lossy, non-invertible, or spuriously plausible transformations that one-way review misses.

## Operational mechanism

Run a forward check from source conditions to proposed result, then independently read the result backward to enumerate which source conditions it actually entails. Compare the reconstructed set with the locked source atoms; missing, invented, or many-to-one-collapsed atoms fail even when the forward narrative is fluent.

## Trigger and task use

Triggers: causal, logical, quantitative, or evidence claims are central. Best-fit tasks: requirements-to-implementation checks, summary-to-source checks, schema migrations, plan-to-objective traceability.

## Interactions and failure boundary

Companions: critical-atomic-verification, citation-fidelity. Failure boundary: Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition..

## Unresolved details / interpretation boundary

The two-direction validation function is directly recovered; the reconstruction procedure makes its distinction operational.
