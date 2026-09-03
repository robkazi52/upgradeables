# Neuro-Focus

## Summary

An attention controller that narrows active processing to the highest-value source region, module, or fault surface while preserving an explicit route back to excluded alternatives.

## Purpose

Increase depth and signal quality on a bounded target when irrelevant material would otherwise dilute effort.

## Problem Solved

Prevents large corpora, long OS documents, or broad codebases from consuming attention equally when only a small region controls the outcome.

## Where It Fits in the OS

Roles: context-retrieval, focus control, planning-reasoning. Pipeline stages: post-intake prioritization, focused execution, checkpoint review.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- large-corpus research
- one-module debugging
- targeted policy review
- high-value constraint analysis

## When Not to Use

- the task requires broad discovery before a target is known
- decisive evidence has not yet been sampled
- narrowing would hide plausible alternatives

## Scope

Canonical package: `neuro-focus@1.1.0`. ID: `A-09`. Functional classes: context-retrieval, planning-reasoning. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- large sources or a narrow debug region demand concentration

## Non-Triggers

- the task requires broad discovery before a target is known
- decisive evidence has not yet been sampled
- narrowing would hide plausible alternatives

## Inputs / Required State

- locked task
- candidate context regions
- relevance/impact criteria
- excluded-region pointers

## Outputs / Produced State

- declared focus corridor
- suppressed-but-recoverable context set
- focused result
- checkpoint expansion decision

## Mechanism

Rank active regions by relevance to the locked task and expected decision impact, choose a bounded focus corridor, suppress unrelated material from the live workspace without deleting it, and periodically test whether excluded regions now contain material counterevidence. The recovered Neuro-Focus purpose and its Anti-Tunnel Vision caution support this normalized control; it is not a neurological claim.

## Procedure

1. Lock the question and define what evidence would make a region high value.
2. Score or order candidate regions by relevance, uncertainty reduction, and consequence.
3. Activate the smallest region sufficient for deep work and retain pointers to excluded regions.
4. Perform the focused analysis or repair.
5. At checkpoints, invoke an alternative scan or Anti-Tunnel Vision test.
6. Expand, shift, or release focus when new evidence changes priority.

## Always-Do Rules

- Make the focus target and exclusion boundary explicit.
- Keep excluded material recoverable.
- Use an anti-fixation checkpoint when alternatives could change the result.

## Never-Do / Avoid Rules

- Do not equate focus with truth or authority.
- Do not permanently discard out-of-focus evidence.
- Do not claim biological or hidden-attention manipulation.

## Interaction Rules

### `activation-budget-funnel`

ABF limits concurrent pulls; Neuro-Focus ranks and deepens the most valuable pull or region.

### `anti-tunnel-vision`

Tests a focused path against credible alternatives before commitment.

## Compatible Upgradeables

- `activation-budget-funnel` — ABF limits concurrent pulls; Neuro-Focus ranks and deepens the most valuable pull or region.
- `anti-tunnel-vision` — Tests a focused path against credible alternatives before commitment.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Prevents deliberate narrowing from becoming fixation or evidence blindness.

## Potential Redundancy

### `scoped-loader`

Loader chooses relevant modules; Neuro-Focus allocates depth among already relevant regions.

### `working-memory-lock-in`

Locks critical items in active state; Neuro-Focus directs processing toward a selected region.

## Conflict / Precedence Rules

- Source coverage and truth gates override the desire to stay narrowly focused.
- If the focus target was selected from incomplete evidence, preserve provisional status and run an alternative scan.

## Failure Boundary

- Relax or move focus when a credible alternative, uncovered dependency, or counterevidence lies outside the corridor.
- Stop claiming adequate coverage if excluded material cannot be recovered for checking.

## Strong-Model Scaling

May skip:

- formal region scoring for a clearly localized task
- frequent focus restatements

Keep mandatory:

- explicit focus boundary
- recoverability of excluded context
- anti-fixation check before commitment

## Recommended Skill Types

- large-corpus research
- one-module debugging
- targeted policy review
- high-value constraint analysis

## Example Composition

**Task context:** Debug a failure in one service within a monorepo.

**Why it activates:** The trace and recent change isolate a narrow high-value area.

**Inputs/state:** Trace, changed files, dependency map, failing test.

**Action:** Concentrates on the implicated module and direct dependencies, then checks one plausible upstream alternative.

**Does not:** It does not scan every repository file or ignore evidence pointing outside the module.

**Result/state change:** A bounded root-cause analysis with an explicit expansion condition.

**Companions:** ['activation-budget-funnel', 'anti-tunnel-vision']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-09` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-09. Neuro-Focus (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — T2-040 — Attention Corridor Narrowing (historical_assistant_artifact)
