# Source Note — Architect Orchestrator

- Slug: `architect-orchestrator`
- ID: `O-01`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)

## Recovered or normalized purpose

Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state.

## Operational mechanism

Translate the locked goal and constraints into a modular plan, select only the necessary OS layers, Genes, Cores, Upgradeables, references, and validators, then coordinate their ordered execution. After execution, run a separate critique, route localized defects to bounded repair, synthesize one result, and emit the minimum continuation state. The orchestrator owns coordination, not every domain operation.

## Trigger and task use

Triggers: designing or refactoring a Skill, OS, framework, or workflow. Best-fit tasks: Skill and OS architecture, workflow design, framework refactoring.

## Interactions and failure boundary

Companions: scoped-loader, state-snapshot. Failure boundary: required module interfaces or authority relationships cannot be resolved; the requested work is domain execution outside the orchestrator's design scope.

## Unresolved details / interpretation boundary

Historical identity, purpose, and core behavior are recovered; v0.2 states the mechanism explicitly without claiming hidden capabilities.
