# Source Note — Structured Refinement Cycles

- Slug: `structured-refinement`
- ID: `T2-02`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-02. Structured Refinement Cycles (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)

## Recovered or normalized purpose

Prevent one revision pass from trading away correctness while improving structure or style.

## Operational mechanism

Classify defects before editing and run passes in dependency order: facts and source mapping first, structure and requirement coverage second, style and pedagogy third, final validation last. Accepted decisions are locked between passes, and a later pass may not silently reopen an earlier one.

## Trigger and task use

Triggers: revision has multiple defect classes. Best-fit tasks: drafts with several defect classes, reports requiring source and style review, prompt or specification cleanup, publication preparation.

## Interactions and failure boundary

Companions: safe-rewrite, bounded-exit, micro-repair. Failure boundary: mixed-objective drift; later-pass regression; style masking factual defects; cycling on globally broken structure.

## Unresolved details / interpretation boundary

The recovered definition explicitly separates factual, structural, style, and final-validation passes and preserves accepted decisions.
