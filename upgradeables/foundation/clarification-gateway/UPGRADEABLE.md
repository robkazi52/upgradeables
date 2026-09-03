# Clarification Gateway

## Summary

A decision gate that separates ambiguity the workflow can safely bound from ambiguity that prevents a correct or authorized result.

## Purpose

Keep clarification proportional: ask only for materially blocking information, otherwise continue with the narrowest explicit assumption or bounded partial result.

## Problem Solved

Avoids both confident execution on missing critical variables and reflexive questioning that stalls work the model could safely complete.

## Where It Fits in the OS

Roles: framing-intake, routing, guard. Pipeline stages: intake, pre-execution, exception-routing.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- requirements intake
- ambiguous data transformation
- multi-constraint planning
- high-stakes evidence work

## When Not to Use

- the missing detail cannot change a valid result
- the host forbids questions and a bounded assumption is safe
- the user already supplied an authoritative value

## Scope

Canonical package: `clarification-gateway@1.1.0`. ID: `T1-03`. Functional classes: framing-intake, orchestration. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- required variables are missing or instructions conflict

## Non-Triggers

- the missing detail cannot change a valid result
- the host forbids questions and a bounded assumption is safe
- the user already supplied an authoritative value

## Inputs / Required State

- task request
- known variables
- authority constraints
- candidate interpretations
- output contract

## Outputs / Produced State

- proceed decision
- focused clarification request
- labeled assumption
- bounded partial-result or abstention status

## Mechanism

Classify each ambiguity by decision impact. If different plausible values would materially change correctness, authority, safety, or the requested deliverable, route to clarification when permitted. Otherwise choose the narrowest labeled assumption, preserve the unresolved field, or return the supported subset; do not turn every uncertainty into a user interruption.

## Procedure

1. Extract missing variables, ambiguous terms, and instruction conflicts before substantive execution.
2. For each item, compare plausible interpretations against the output contract and authority rules.
3. Mark an item blocking only when the interpretations lead to materially different valid actions or conclusions.
4. Ask one focused question for blocking items when interaction is available; otherwise state the narrow assumption or limit the result.
5. Record the answer or assumption in task state so the same ambiguity is not reopened without new evidence.

## Always-Do Rules

- Explain why a requested clarification changes the result.
- Prefer one consolidated, answerable question over serial interrogation.
- Label assumptions and unsupported branches.

## Never-Do / Avoid Rules

- Do not ask for information already present in the supplied state.
- Do not silently select a consequential interpretation.
- Do not use clarification as a substitute for ordinary analysis.

## Interaction Rules

### `task-set-lock-in`

Writes confirmed answers and bounded assumptions into the locked task definition so downstream work uses one interpretation.

## Compatible Upgradeables

- `task-set-lock-in` — Writes confirmed answers and bounded assumptions into the locked task definition so downstream work uses one interpretation.

## Counterbalancing Upgradeables

### `bounded-exit`

Prevents clarification loops by terminating once the minimum blocking information is obtained or a bounded fallback is selected.

## Potential Redundancy

### `task-set-lock-in`

Task-Set Lock-In stores resolved task fields; Clarification Gateway decides which unresolved fields require intervention.

## Conflict / Precedence Rules

- A higher-authority instruction not to ask questions converts the gate into assumption selection, not permission to ignore ambiguity.
- If no safe bounded assumption exists for a consequential decision, return the supported subset or abstain.

## Failure Boundary

- Stop or narrow when a required variable has multiple materially different interpretations and neither clarification nor a safe assumption is available.

## Strong-Model Scaling

May skip:

- an explicit ambiguity table for straightforward cases
- asking when context uniquely resolves the variable

Keep mandatory:

- materiality test
- assumption labeling
- authority-sensitive fallback

## Recommended Skill Types

- high-stakes evidence work
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A user asks for a shipping quote but gives a city shared by two states.

**Why it activates:** Destination changes price and feasibility.

**Inputs/state:** City supplied; state and postal code absent; questions permitted.

**Action:** Asks one focused destination question before pricing and records the answer.

**Does not:** It does not guess the state or ask unrelated preference questions.

**Result/state change:** A resolved destination field or an explicit inability to quote.

**Companions:** ['task-set-lock-in']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Clarification-First, Clarification-First Behavior.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — January 5 scaffolding classification (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — `UPGRADEABLE_ACTIVATION_TIERS_T1` (historical_assistant_artifact)
