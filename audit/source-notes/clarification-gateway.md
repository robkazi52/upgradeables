# Source Note — Clarification Gateway

- Slug: `clarification-gateway`
- ID: `T1-03`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — January 5 scaffolding classification (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `UPGRADEABLE_ACTIVATION_TIERS_T1` (historical_assistant_artifact)

## Recovered or normalized purpose

Keep clarification proportional: ask only for materially blocking information, otherwise continue with the narrowest explicit assumption or bounded partial result.

## Operational mechanism

Classify each ambiguity by decision impact. If different plausible values would materially change correctness, authority, safety, or the requested deliverable, route to clarification when permitted. Otherwise choose the narrowest labeled assumption, preserve the unresolved field, or return the supported subset; do not turn every uncertainty into a user interruption.

## Trigger and task use

Triggers: required variables are missing or instructions conflict. Best-fit tasks: requirements intake, ambiguous data transformation, multi-constraint planning, high-stakes evidence work.

## Interactions and failure boundary

Companions: task-set-lock-in. Failure boundary: Stop or narrow when a required variable has multiple materially different interpretations and neither clarification nor a safe assumption is available..

## Unresolved details / interpretation boundary

The catalog directly recovers the materiality test, ask-only-when-needed rule, and best-effort assumption fallback; no direct package-specific mention was located in the Deep Context Addendum.
