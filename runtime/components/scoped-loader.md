# Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)

Purpose: Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start.

Activate when: a modular workflow has multiple available components.

Do not use when: the workflow has one small fixed instruction set; selection criteria are unavailable.

Requires: none.

## Runtime mechanism

Resolve the active task first, then load in recovered authority/function order: task shell, applicable Behavior Gene, authorized Core, only triggered Upgradeables, references or resources on demand, and validators before commitment. Record what was loaded and why; leave unrelated modules inactive so their rules and context cannot leak into the task.

## Procedure

1. Classify the task, domain, mode, risk, and output contract.
2. Load the task shell and its authority constraints.
3. Load at most the required Behavior Gene and authorized Core/reference layer.
4. Evaluate Upgradeable triggers and dependencies, then activate only the minimal matching set.
5. Fetch deep references, resources, or tools only when a retained component needs them.

## Guardrails

- Mandatory even on strong models: task-first selection; authority-ordered loading; inactive-by-default treatment of unrelated modules.
- Conflict/precedence: Host/system and task authority determine eligibility; relevance alone cannot authorize a module; If two loaders disagree, prefer the route tied to the locked task and explicit manifests, or escalate rather than merging all candidates.
- Stop or fail when: Do not load a component when its trigger, authority, dependency, or host capability cannot be established; Escalate when required components conflict and precedence cannot resolve them.

Full package and provenance: [`scoped-loader`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md).
