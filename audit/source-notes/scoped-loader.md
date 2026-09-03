# Source Note — Scoped Loader / Loader Sequencing

- Slug: `scoped-loader`
- ID: `T1-07`
- Source support: `sufficiently-recovered`
- Mechanism basis: `recovered`
- Final status: `PASS`

## Recovered facts and source anchors

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-07. Loader Sequencing (current_consolidated_catalog)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.2 Research Intake / Corpus Map (historical_assistant_artifact)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Canonical current consolidated inventory (historical_recovery_inventory)

## Recovered or normalized purpose

Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start.

## Operational mechanism

Resolve the active task first, then load in recovered authority/function order: task shell, applicable Behavior Gene, authorized Core, only triggered Upgradeables, references or resources on demand, and validators before commitment. Record what was loaded and why; leave unrelated modules inactive so their rules and context cannot leak into the task.

## Trigger and task use

Triggers: a modular workflow has multiple available components. Best-fit tasks: modular Skill execution, agent routing, large reference libraries, domain OS selection, multi-stage research.

## Interactions and failure boundary

Companions: activation-budget-funnel, task-set-lock-in. Failure boundary: Do not load a component when its trigger, authority, dependency, or host capability cannot be established.; Escalate when required components conflict and precedence cannot resolve them..

## Unresolved details / interpretation boundary

The catalog recovers an explicit seven-step load sequence and prohibition on loading the full library; later sources confirm scoped loading in research and intake workflows.
