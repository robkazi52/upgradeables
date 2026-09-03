# Temporal Anchor Scaffold

## Summary

Temporarily organize dates, event order, effective windows, and unresolved temporal relations so time-dependent claims can be evaluated correctly.

## Purpose

Prevent chronology errors and confusion between event time, publication time, and current validity.

## Problem Solved

Documents often mix dated facts, relative phrases, revised policies, and unknown ordering; narrative context alone makes temporal mistakes likely.

## Where It Fits in the OS

Roles: temporal normalization, task-local scaffold, sequence validation. Pipeline stages: source intake, timeline reconciliation, time-sensitive reasoning, final citation check.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- incident timelines
- policy version analysis
- case chronology
- news or market research

## When Not to Use

- time has no bearing on the answer
- dates are fabricated or inferred without support
- a mature temporal database already supplies the needed view

## Scope

Canonical package: `temporal-anchor-scaffold@1.1.0`. ID: `JAN26-07`. Functional classes: state, truth-grounding. Activation: `U1-common-conditional`. Mechanism basis: `provisional`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- time or chronology affects correctness

## Non-Triggers

- time has no bearing on the answer
- dates are fabricated or inferred without support
- a mature temporal database already supplies the needed view

## Inputs / Required State

- dated source excerpts
- reference date
- timezone
- event identities
- effective-window rules

## Outputs / Produced State

- normalized task-local timeline
- ordering constraints
- temporal uncertainty flags
- promotable verified anchors

## Mechanism

A modern interpretation is a task-local table of events with normalized timestamp or interval, original temporal expression, source, event/publication/effective-time type, confidence, and before/after links. Unknown order stays unknown. Promote only durable verified temporal facts into canonical state and retire the scaffold after the timeline-dependent output is validated.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify which temporal distinctions affect the decision.
2. Extract expressions verbatim with source pointers.
3. Normalize only supported dates, zones, intervals, and time types.
4. Build explicit ordering links and mark ambiguity or contradiction.
5. Use the scaffold to test time-dependent claims.
6. Promote verified durable dates if needed, then delete or archive the task-local scaffold.

## Always-Do Rules

- distinguish event, publication, observation, and effective time
- retain original expressions
- label uncertainty and timezone
- retire the temporary scaffold

## Never-Do / Avoid Rules

- invent missing dates
- resolve ambiguous relative time from conversational recency alone
- carry the whole scaffold as permanent state by default

## Interaction Rules

### `state-snapshot`

A snapshot supplies a trusted state time point against which events can be reconciled.

### `sequential-memory-state-engine`

Consumes ordered, provenance-bearing events after temporal normalization.

### `micro-scaffolding`

Provides the same temporary-build/promote/retire lifecycle specialized for chronology.

## Compatible Upgradeables

- `state-snapshot` — A snapshot supplies a trusted state time point against which events can be reconciled.
- `sequential-memory-state-engine` — Consumes ordered, provenance-bearing events after temporal normalization.
- `micro-scaffolding` — Provides the same temporary-build/promote/retire lifecycle specialized for chronology.

## Counterbalancing Upgradeables

### `clarification-gateway`

Requests a reference date or timezone when ambiguity changes the answer.

### `stable-long-context`

Keeps only durable temporal anchors active after the local timeline work ends.

## Potential Redundancy

### `sequential-memory-state-engine`

SMSE owns ordered state transitions; this scaffold only resolves a difficult local chronology before ingestion.

### `state-snapshot`

Snapshot captures one known time, not an event relationship graph.

## Conflict / Precedence Rules

- Source-stated timestamps outrank inferred order; higher-authority corrections supersede earlier dates while retaining history.
- If timezone or effective date changes the conclusion and cannot be resolved, surface the branch rather than choosing one.

## Failure Boundary

- Do not assert total order from partial temporal evidence.
- Treat the mechanism as provisional until original concept-specific documentation is recovered.

## Strong-Model Scaling

May skip:

- a formal table when two explicit dates suffice
- promotion of dates irrelevant beyond the immediate result

Keep mandatory:

- time-type distinction
- source pointers
- explicit unknown order
- retirement after use

## Recommended Skill Types

- incident timelines
- policy version analysis
- case chronology
- news or market research

## Example Composition

**Task context:** Determine which of three policy versions governed an incident.

**Why it activates:** Publication date, effective date, and incident time differ.

**Inputs/state:** Three cited version notices, incident timestamp, timezone, and one ambiguous relative phrase.

**Action:** Builds a temporary typed timeline, flags the ambiguity, and tests applicability windows.

**Does not:** It does not equate publication with effectiveness or guess the relative date.

**Result/state change:** The applicable version is identified with an explicit uncertainty branch.

**Companions:** ['clarification-gateway', 'sequential-memory-state-engine', 'state-snapshot']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-07` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 1. Canonical current consolidated inventory (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `GLOBAL_LOCAL_ANCHOR_SPLIT_T1` (historical_assistant_artifact)
