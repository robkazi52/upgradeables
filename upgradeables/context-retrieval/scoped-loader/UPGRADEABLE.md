# Scoped Loader / Loader Sequencing

## Summary

A deterministic load-order controller that admits only the task shell, behavior, knowledge, controls, references, tools, and validators needed for the active job.

## Purpose

Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start.

## Problem Solved

Prevents authority confusion, context bloat, irrelevant rule activation, and premature access to references or tools that the current task does not require.

## Where It Fits in the OS

Roles: context-retrieval, orchestration, capability routing. Pipeline stages: task classification, pre-retrieval, on-demand loading, pre-commit validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- modular Skill execution
- agent routing
- large reference libraries
- domain OS selection
- multi-stage research

## When Not to Use

- the workflow has one small fixed instruction set
- selection criteria are unavailable
- loading a component would exceed host capability or authority

## Scope

Canonical package: `scoped-loader@1.1.0`. ID: `T1-07`. Functional classes: context-retrieval, orchestration. Activation: `U0-foundational`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a modular workflow has multiple available components

## Non-Triggers

- the workflow has one small fixed instruction set
- selection criteria are unavailable
- loading a component would exceed host capability or authority

## Inputs / Required State

- task classification
- authority hierarchy
- component manifests
- trigger/dependency data
- host capabilities

## Outputs / Produced State

- ordered minimal load plan
- active component list
- deferred resource pointers
- activation rationale and unresolved conflicts

## Mechanism

Resolve the active task first, then load in recovered authority/function order: task shell, applicable Behavior Gene, authorized Core, only triggered Upgradeables, references or resources on demand, and validators before commitment. Record what was loaded and why; leave unrelated modules inactive so their rules and context cannot leak into the task.

## Procedure

1. Classify the task, domain, mode, risk, and output contract.
2. Load the task shell and its authority constraints.
3. Load at most the required Behavior Gene and authorized Core/reference layer.
4. Evaluate Upgradeable triggers and dependencies, then activate only the minimal matching set.
5. Fetch deep references, resources, or tools only when a retained component needs them.
6. Activate applicable validators before final commitment and emit a load record.

## Always-Do Rules

- Resolve authority before loading lower-level behavior.
- Document activation reasons and unavailable capabilities.
- Prefer deterministic indexes or manifests when the host supports them.

## Never-Do / Avoid Rules

- Do not load the entire component library by default.
- Do not treat routing to a reference as proof that its contents apply.
- Do not let a loaded component override the task or host policy.

## Interaction Rules

### `activation-budget-funnel`

After the loader selects relevant material, ABF stages how much of it may be active and processed at once.

### `task-set-lock-in`

Supplies the task identity and constraints used to make load decisions.

## Compatible Upgradeables

- `activation-budget-funnel` — After the loader selects relevant material, ABF stages how much of it may be active and processed at once.
- `task-set-lock-in` — Supplies the task identity and constraints used to make load decisions.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Checks whether narrow loading excluded a plausible source or capability needed for the result.

## Potential Redundancy

### `activation-budget-funnel`

Both reduce context burden, but loader decides relevance/order while ABF controls concurrent activation and processing stages.

## Conflict / Precedence Rules

- Host/system and task authority determine eligibility; relevance alone cannot authorize a module.
- If two loaders disagree, prefer the route tied to the locked task and explicit manifests, or escalate rather than merging all candidates.

## Failure Boundary

- Do not load a component when its trigger, authority, dependency, or host capability cannot be established.
- Escalate when required components conflict and precedence cannot resolve them.

## Strong-Model Scaling

May skip:

- verbose load manifests for a tiny fixed workflow
- separate loading calls when the host safely bundles a small compatible set

Keep mandatory:

- task-first selection
- authority-ordered loading
- inactive-by-default treatment of unrelated modules

## Recommended Skill Types

- modular Skill execution
- agent routing
- large reference libraries
- domain OS selection
- multi-stage research

## Example Composition

**Task context:** Answer a legal research question from a mixed policy library.

**Why it activates:** Multiple Genes, Cores, sources, and validators are available.

**Inputs/state:** Locked jurisdiction, research question, component index, and source permissions.

**Action:** Loads the research shell, applicable legal references, grounding and citation controls, then the needed sources and final validators.

**Does not:** It does not load medical Cores, creative modes, or the complete policy archive.

**Result/state change:** A small authority-ordered active stack with an auditable load record.

**Companions:** ['task-set-lock-in', 'activation-budget-funnel']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-07` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Loader Sequencing, Loader.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-07. Loader Sequencing (current_consolidated_catalog)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 11.2 Research Intake / Corpus Map (historical_assistant_artifact)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Canonical current consolidated inventory (historical_recovery_inventory)
