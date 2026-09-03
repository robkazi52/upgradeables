# Source Note — Safe Rewrite Logic

- Slug: `safe-rewrite`
- ID: `T1-10`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-10. Safe Rewrite Logic (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW — EXAMPLE OF UPGRADEABLE COMPOSITION (historical_assistant_artifact)

## Recovered or normalized purpose

Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions.

## Operational mechanism

Extract a before-state ledger of factual and constraint atoms, mark the dimensions authorized to change, perform the rewrite only along those dimensions, then compare names, numbers, dates, quotes, citations, modality, requirements, and causal claims. Any atom difference not explicitly authorized is reverted or surfaced for approval.

## Trigger and task use

Triggers: paraphrasing, polishing, or format conversion. Best-fit tasks: paraphrasing, tone adjustment, format conversion, clarity polishing, audience adaptation.

## Interactions and failure boundary

Companions: micro-repair, citation-fidelity, style-alignment. Failure boundary: semantic drift; citation drift; lost negation or uncertainty; unrequested content addition; meaning change hidden as polish.

## Unresolved details / interpretation boundary

The recovered source directly lists preservation of factual atoms and explicit rechecks for names, numbers, dates, quotes, and citations.
