# Anti-Tunnel Vision

## Summary

Keeps a solver from treating its first plausible explanation or plan as settled before testing a small number of credible rivals.

## Purpose

Preserve enough search breadth to expose premature fixation, then collapse quickly when evidence discriminates.

## Problem Solved

A favored hypothesis can silently determine evidence selection, diagnosis, and design even when a nearby alternative explains the same facts better.

## Where It Fits in the OS

Roles: reasoning control, premature-convergence guard. Pipeline stages: hypothesis formation, plan selection, pre-commit review.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- ambiguous diagnosis
- architecture choice with two credible patterns
- research synthesis with competing explanations

## When Not to Use

- the answer is directly established by a locked source
- a safety or policy veto already determines the outcome
- branching cost exceeds the bounded decision value

## Scope

Canonical package: `anti-tunnel-vision@1.1.0`. ID: `T2-19`. Functional classes: planning-reasoning, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires premature fixation is plausible.

## Non-Triggers

- the answer is directly established by a locked source
- a safety or policy veto already determines the outcome
- branching cost exceeds the bounded decision value

## Inputs / Required State

- favored candidate
- task constraints
- available discriminating evidence
- exploration budget

## Outputs / Produced State

- bounded rival set
- discriminating comparison
- selected path or explicit residual uncertainty

## Mechanism

Name the leading path and at least one genuinely plausible competitor, specify the observation that would distinguish them, and compare only on that discriminating evidence. The controller is bounded: it prevents first-path lock-in without turning every task into open-ended brainstorming.

## Procedure

1. State the current favored hypothesis or plan and the evidence supporting it.
2. Generate one or two materially different competitors, not cosmetic restatements.
3. For each candidate, identify its strongest confirming signal and strongest disconfirming signal.
4. Acquire or inspect the cheapest decisive evidence available.
5. Select, synthesize, or explicitly preserve uncertainty; retire alternatives that lose on the discriminating evidence.

## Always-Do Rules

- make the favored path explicit
- require competitors to differ in causal account or implementation strategy
- define a stopping condition before expanding the search

## Never-Do / Avoid Rules

- invent weak straw alternatives merely to satisfy a count
- keep rejected branches active after decisive evidence
- override a hard truth or safety constraint in the name of exploration

## Interaction Rules

### `multiverse-reasoning`

Multiverse supplies bounded candidates; Anti-Tunnel Vision checks that the candidate set is not just the initial idea in several phrasings.

### `dominant-driver-isolation-scaffold`

Driver isolation can test which rival causal explanation accounts for the highest-impact evidence.

## Compatible Upgradeables

- `multiverse-reasoning` — Multiverse supplies bounded candidates; Anti-Tunnel Vision checks that the candidate set is not just the initial idea in several phrasings.
- `dominant-driver-isolation-scaffold` — Driver isolation can test which rival causal explanation accounts for the highest-impact evidence.

## Counterbalancing Upgradeables

### `neuro-focus`

Neuro-Focus narrows attention after Anti-Tunnel Vision has ensured that narrowing is earned.

## Potential Redundancy

### `multiverse-reasoning`

Both resist premature commitment, but this module is a fixation guard while Multiverse is a branch-generation and selection procedure.

## Conflict / Precedence Rules

- If a hard veto eliminates a branch, do not keep it alive for balance.
- When evidence cannot discriminate within budget, report unresolved alternatives instead of manufacturing certainty.

## Failure Boundary

- unbounded ideation
- token alternatives with no material difference
- false balance after decisive evidence
- analysis paralysis

## Strong-Model Scaling

May skip:

- writing a formal comparison table when only one quick rival check is needed

Keep mandatory:

- explicitly test at least one plausible rival before a costly commitment
- retain the stop rule

## Recommended Skill Types

- ambiguous diagnosis
- architecture choice with two credible patterns
- research synthesis with competing explanations

## Example Composition

**Task context:** A service is slow after a deployment.

**Why it activates:** The team has fixated on the new database query although saturation and cache invalidation are also plausible.

**Inputs/state:** Latency rose at deploy time; query timing, CPU saturation, and cache hit-rate data are available.

**Action:** Compares query regression against cache invalidation using the cheapest discriminating metrics, then selects the explanation supported by timing and cache data.

**Does not:** List every imaginable outage cause or preserve the query hypothesis after contrary evidence.

**Result/state change:** A bounded, evidence-selected diagnosis with one residual uncertainty noted.

**Companions:** ['dominant-driver-isolation-scaffold', 'multiverse-reasoning']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-19` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-19. Anti-Tunnel Vision (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
