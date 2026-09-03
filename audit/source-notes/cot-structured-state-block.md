# Source Note — CoT-Structured State Block

- Slug: `cot-structured-state-block`
- ID: `STATE-2025-12-03-T3`
- Source support: `strongly-derivable`
- Mechanism basis: `modern-interpretation`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)

## Recovered or normalized purpose

Make reasoning-relevant state portable and auditable while preserving the boundary between useful state and hidden internal deliberation.

## Operational mechanism

Maintain an explicit schema of externally useful reasoning state: verified facts with provenance, user-provided constraints, labeled assumptions, concise conclusion summaries, unresolved questions, confidence, and next action. The block records what another worker needs to continue; it never stores token-level private deliberation or presents inference as evidence.

## Trigger and task use

Triggers: structured intermediate task state must survive across steps. Best-fit tasks: multi-agent research, long investigations, regulated decisions, work requiring resumable rationale.

## Interactions and failure boundary

Companions: stateblock, structured-state-projection, state-snapshot. Failure boundary: Stop treating the block as authoritative if provenance is missing or fields are stale.; Do not use the pattern to satisfy requests for hidden chain-of-thought..

## Unresolved details / interpretation boundary

The exact recovered label has limited prose, so the safe mechanism is a modern operationalization grounded in the addendum's structured-state and provenance architecture; it explicitly excludes private chain-of-thought.
