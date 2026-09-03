# Reasoning-Scale Controller

## Summary

Selects the smallest adequate reasoning scale from fact-level inspection through global architecture, then changes scale only on explicit complexity or risk signals.

## Purpose

Match reasoning depth and scope to the unit of work instead of applying either shallow local analysis or system-wide architecture indiscriminately.

## Problem Solved

Models overthink simple transformations, underthink coupled high-risk tasks, or mix local sentence repair with global architecture decisions.

## Where It Fits in the OS

Roles: reasoning depth controller, scope router. Pipeline stages: task triage, reasoning execution, escalation and de-escalation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- mixed-complexity workflows
- long-form construction
- system design
- quality evaluation

## When Not to Use

- a governing workflow already fixes the required scale
- the unit is safety-critical and policy mandates the highest review tier
- scale labels would replace rather than guide actual reasoning

## Scope

Canonical package: `reasoning-scale-controller@1.1.0`. ID: `RS-00`. Functional classes: planning-reasoning, meta-control. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- task complexity or risk requires depth selection

## Non-Triggers

- a governing workflow already fixes the required scale
- the unit is safety-critical and policy mandates the highest review tier
- scale labels would replace rather than guide actual reasoning

## Inputs / Required State

- task unit
- dependency span
- uncertainty
- risk and reversibility
- quality requirements

## Outputs / Produced State

- selected reasoning scale
- escalation or de-escalation decisions
- scope-appropriate reasoning artifact

## Mechanism

Route work through one controller: Subatomic for a fact, local relation, constraint, or sentence decision; Atomic for a small verified inference or action; Nano as a light intermediate structure whose detailed historical spec remains unrecovered; Micro for task-local scaffolds and dependencies; QMS for quality evaluation; Cosmic for global architecture, strategy, or long-horizon planning. Escalate when dependency span, ambiguity, irreversibility, or risk exceeds the current scale; de-escalate after the larger question is resolved.

## Procedure

1. Identify the unit of work, dependency radius, uncertainty, and consequence of error.
2. Choose the lowest scale that can represent all relevant dependencies.
3. Execute only the operations appropriate to that scale.
4. Escalate one or more levels when local reasoning exposes unresolved cross-unit dependencies, competing quality dimensions, or global architecture effects.
5. After the higher-scale decision, return local implementation to the smallest adequate scale and record the boundary.

## Always-Do Rules

- start at the smallest adequate scale
- escalate on concrete signals rather than prestige
- preserve global constraints when returning to local work
- keep Nano semantics modest because its detailed historical specification is unrecovered

## Never-Do / Avoid Rules

- use Cosmic for a sentence edit
- solve architecture from isolated facts without aggregation
- invent a detailed historical Nano algorithm
- confuse QMS evaluation with generation

## Interaction Rules

### `cognitive-governor`

The governor budgets effort after the scale controller identifies the required scope.

### `dynamic-depth-allocation`

Dynamic allocation varies effort within the selected scale as evidence and difficulty change.

### `micro-scaffolding`

Micro-Scaffolding structures task-local dependencies when the controller selects Micro scale.

## Compatible Upgradeables

- `cognitive-governor` — The governor budgets effort after the scale controller identifies the required scope.
- `dynamic-depth-allocation` — Dynamic allocation varies effort within the selected scale as evidence and difficulty change.
- `micro-scaffolding` — Micro-Scaffolding structures task-local dependencies when the controller selects Micro scale.

## Counterbalancing Upgradeables

### `bounded-exit`

Bounded ExIt caps repeated work at any selected scale.

### `critical-atomic-verification`

Atomic verification prevents scale escalation from resting on bad fact-level units.

## Potential Redundancy

### `dynamic-depth-allocation`

Both tune reasoning effort, but the scale controller selects semantic scope while dynamic allocation adjusts depth or budget.

## Conflict / Precedence Rules

- Risk-mandated review overrides the desire to stay at a cheaper scale.
- Cosmic conclusions must be decomposed back into verifiable local units before execution.
- Nano may be used only as a light intermediate label until historical mechanics are recovered.

## Failure Boundary

- scale theater
- chronic overthinking
- local reasoning that ignores global dependencies
- invented Nano mechanics
- global plans without local verification

## Strong-Model Scaling

May skip:

- printing scale names on routine tasks
- stepping through every intermediate scale when direct routing is obvious

Keep mandatory:

- smallest-adequate-scope selection
- explicit escalation signals
- global-to-local decomposition

## Recommended Skill Types

- analysis and decision support
- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Correct one citation in a long report whose architecture is already accepted.

**Why it activates:** The surrounding artifact is large, but the actual defect is local and source-verifiable.

**Inputs/state:** The correct source passage and locked report structure are available.

**Action:** Routes source verification to Subatomic, the citation replacement to Atomic, and avoids Cosmic redesign unless the correction exposes a section-wide provenance failure.

**Does not:** Re-outline the report because the document is long.

**Result/state change:** A proportional local correction with an explicit escalation condition.

**Companions:** ['critical-atomic-verification', 'micro-repair']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `RS-00` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.5 Section / paragraph micro-scaffolding (historical_assistant_artifact)
