# Source Note — Domain / Mode Isolation

- Slug: `domain-mode-isolation`
- ID: `T3-10`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 14. Domain OS / bundle instances (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)

## Recovered or normalized purpose

Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts.

## Operational mechanism

Create a named compartment for each active domain with its own instructions, terms, sources, permissions, and state. Route new material into the matching compartment; make cross-domain transfer an explicit projection with provenance, and validate the final output against the selected domain rather than the union of all modes.

## Trigger and task use

Triggers: multiple domains or semantic modes coexist. Best-fit tasks: mixed-domain workspaces, multi-tenant assistants, regulated workflows, parallel specialist agents.

## Interactions and failure boundary

Companions: mode-lock-in, structured-state-projection, scoped-loader. Failure boundary: Pause when the domain is ambiguous and different classifications change safety or authority.; Do not claim isolation if the host cannot control context or tool exposure; emulate with explicit labels and validation..

## Unresolved details / interpretation boundary

Direct catalog guidance and the addendum's domain-isolation example support the compartment-and-projection mechanism.
