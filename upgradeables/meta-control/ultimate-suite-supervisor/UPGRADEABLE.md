# Ultimate Suite Supervisor

## Summary

Acts as the top-level suite authority for mode declaration, Core-stack enforcement, local-versus-global editing, pack conflicts, intensity, and post-output health.

## Purpose

Keep a large OS or skill suite operating as one authority-consistent system across planning, execution, repair, and finalization.

## Problem Solved

A suite can have individually sound modules yet fail globally when modes are implicit, required Cores are skipped, editors overlap, packs conflict, or no owner performs the final health decision.

## Where It Fits in the OS

Roles: top-level suite supervisor, global mode and authority arbiter. Pipeline stages: suite activation, mode and stack declaration, global routing, conflict resolution, post-output health gate.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- large modular OS execution
- multi-mode skill suites
- complex authoring or research systems
- architecture plus execution pipelines

## When Not to Use

- one small skill can complete the task
- only process-health repair is needed
- the suite manifest or authority rules are unavailable

## Scope

Canonical package: `ultimate-suite-supervisor@1.1.0`. ID: `T4-05`. Functional classes: meta-control, orchestration, validation. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a large suite needs top-level coordination

## Non-Triggers

- one small skill can complete the task
- only process-health repair is needed
- the suite manifest or authority rules are unavailable

## Inputs / Required State

- suite manifest
- task and risk
- host capabilities
- Core, Gene, and module contracts
- authority and health criteria

## Outputs / Produced State

- suite execution contract
- declared mode and stack
- resolved module routing
- edit-class and intensity decisions
- final suite health status

## Mechanism

Build a suite execution contract that declares active mode, required Core and Gene stack, authorized modules, authority precedence, edit class, duration and intensity, transition rules, and final health criteria. Delegate local process monitoring and repair to Meta-Supervisor, but retain decisions that affect the whole suite: POWER/SAFE/HYBRID, required stack enforcement, CRISPR versus Surgery, cross-pack conflicts, and post-output acceptance. Emit one authoritative routing state and fail closed on unresolved global conflict.

## Procedure

1. Load the suite manifest, task, host capabilities, risk, and authority rules.
2. Declare the active operating mode and required Core, Gene, Upgradeable, state, and validation stack.
3. Resolve activation conflicts and select local CRISPR or global Surgery editing when changes arise.
4. Set duration, intensity, transition gates, and one owner for each component result.
5. Delegate process-health monitoring and bounded repairs to Meta-Supervisor while retaining global authority decisions.
6. Run post-output checks for grounding, contradiction, tone, drift, stack compliance, and unresolved conflicts; commit or fail closed.

## Always-Do Rules

- declare mode explicitly
- enforce the required Core stack
- resolve authority before activation
- choose edit scale explicitly
- own the final suite health decision

## Never-Do / Avoid Rules

- activate the full suite by default
- duplicate Meta-Supervisor's local repair work
- allow two packs authority over the same decision
- approve output with unresolved global conflict

## Interaction Rules

### `meta-supervisor`

Meta-Supervisor handles runtime health diagnosis and bounded repair under the suite contract.

### `hybrid-mode`

Ultimate Suite declares and gates POWER-to-SAFE transitions.

### `behavior-gene-builder`

Built Genes are loaded only when required by the declared Core and task stack.

### `domain-core-builder`

The required Core stack supplies domain knowledge separate from behaviors.

## Compatible Upgradeables

- `meta-supervisor` — Meta-Supervisor handles runtime health diagnosis and bounded repair under the suite contract.
- `hybrid-mode` — Ultimate Suite declares and gates POWER-to-SAFE transitions.
- `behavior-gene-builder` — Built Genes are loaded only when required by the declared Core and task stack.
- `domain-core-builder` — The required Core stack supplies domain knowledge separate from behaviors.

## Counterbalancing Upgradeables

### `scoped-loader`

Scoped loading prevents top-level supervision from becoming full-suite activation.

### `reasoning-throughput-governor`

Throughput constrains coordination overhead and active breadth.

## Potential Redundancy

### `meta-supervisor`

Meta-Supervisor monitors and repairs process health; Ultimate Suite controls global modes, stack, edit class, cross-pack authority, intensity, and final acceptance.

### `architect-orchestrator`

Architect designs or assembles systems; Ultimate Suite operates and governs an instantiated suite.

## Conflict / Precedence Rules

- Truth, safety, and explicit user authority outrank suite preferences.
- A cross-pack authority conflict blocks the affected action until resolved.
- Meta-Supervisor cannot change global mode or Core stack without escalation.
- Unavailable required components produce a fallback or blocker, never simulated activation.

## Failure Boundary

- monolithic full-suite loading
- supervisor role collapse
- implicit mode
- authority race
- wrong edit scale
- rubber-stamp final health

## Strong-Model Scaling

May skip:

- verbose suite contract rendering when a machine-readable manifest already captures it
- top-level supervision for a one-component low-risk task

Keep mandatory:

- mode declaration
- required-stack check
- global conflict authority
- edit-scale choice
- final health gate

## Recommended Skill Types

- high-stakes evidence work
- multi-step task execution
- review and quality assurance
- skill and agent workflows

## Example Composition

**Task context:** Run a modular evidence-authoring suite to produce and publish a sourced report.

**Why it activates:** The workflow needs a Domain Core, authoring Gene, POWER planning, SAFE drafting, repair packs, and final grounding and style checks.

**Inputs/state:** Suite manifest, source corpus, risk tier, module contracts, and publication criteria are available.

**Action:** Declares HYBRID, loads the required Core and Gene, gates the transition, delegates a local loop to Meta-Supervisor, chooses CRISPR for one citation defect, and owns final health acceptance.

**Does not:** Have Meta-Supervisor redesign the report architecture or load every available module.

**Result/state change:** One authority-consistent suite execution with an auditable final gate.

**Companions:** ['meta-supervisor', 'hybrid-mode', 'loader-sequencing']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-05` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 15.2 Historical Meta-OS template (historical_assistant_artifact)
