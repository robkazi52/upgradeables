# Future-Proof Mode Selector

## Summary

Selects an operating profile from observed host capability, environment support, and task risk rather than hard-coding one scaffold for every model.

## Purpose

Keep workflows portable across frontier and smaller models, tool environments, and future hosts without weakening invariant controls.

## Problem Solved

A workflow tuned to one host either burdens stronger systems with obsolete scaffolding or silently assumes tools, context, state, and reliability weaker hosts do not possess.

## Where It Fits in the OS

Roles: host-capability mode router, portability controller. Pipeline stages: capability probe, task-risk assessment, mode selection, fallback routing.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- cross-model skill packages
- tool-optional workflows
- portable agent systems
- deployments with different context and persistence support

## When Not to Use

- the host and task profile are fixed
- capability cannot be tested and no conservative fallback exists
- selection would alter non-negotiable truth or safety rules

## Scope

Canonical package: `future-proof-mode-selector@1.1.0`. ID: `T4-17`. Functional classes: meta-control, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `normalized-from-recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- an implementation targets models with different capabilities

## Non-Triggers

- the host and task profile are fixed
- capability cannot be tested and no conservative fallback exists
- selection would alter non-negotiable truth or safety rules

## Inputs / Required State

- host capability evidence
- environment tools and permissions
- state and context support
- task risk
- available mode profiles

## Outputs / Produced State

- selected operating profile
- enabled and omitted controls
- fallback route
- selection rationale

## Mechanism

Probe real host affordances—context, tools, state persistence, structured outputs, reliability evidence, and execution permissions—then combine them with task risk to choose a named light, standard, or heavy scaffold profile. Use model-size drift scaling as one capability signal, never as the selector itself; capability claims must be observed or declared, and truth, safety, state, and integrity invariants remain mandatory in every profile.

## Procedure

1. Declare the task's risk, state, tool, and validation requirements.
2. Probe or read the host's actual capabilities and permissions without assuming hidden persistence or tools.
3. Map capability and risk to a predeclared operating profile with explicit enabled and omitted controls.
4. Run a readiness check and select a conservative fallback when any required affordance is absent.
5. Monitor failures that invalidate the profile and switch modes at a checkpoint.
6. Record the chosen profile and reasons so behavior remains reproducible across hosts.

## Always-Do Rules

- test capabilities rather than infer them from brand or model size
- preserve invariant controls across profiles
- provide a conservative fallback
- record selection rationale

## Never-Do / Avoid Rules

- assume a larger model has tools or persistence
- remove truth or safety gates as an optimization
- silently change modes mid-action
- encode one vendor's interface as universal semantics

## Interaction Rules

### `model-size-drift-scaling`

DSS-MS supplies a reliability-to-scaffolding scaling policy that FPMS uses alongside environment and risk.

### `risk-tier-scaling`

Risk Tier prevents a capable host from selecting an undercontrolled profile for consequential work.

### `adapter-first-experimentation`

Unsupported or novel host capabilities can be integrated as optional adapters.

## Compatible Upgradeables

- `model-size-drift-scaling` — DSS-MS supplies a reliability-to-scaffolding scaling policy that FPMS uses alongside environment and risk.
- `risk-tier-scaling` — Risk Tier prevents a capable host from selecting an undercontrolled profile for consequential work.
- `adapter-first-experimentation` — Unsupported or novel host capabilities can be integrated as optional adapters.

## Counterbalancing Upgradeables

### `safe-mode`

SAFE provides the conservative fallback when capability or environment support is uncertain.

## Potential Redundancy

### `model-size-drift-scaling`

DSS-MS adjusts scaffolding as model reliability changes; FPMS makes the actual multi-factor mode choice including tools, state, permissions, and task risk.

## Conflict / Precedence Rules

- Task-risk requirements override host convenience.
- Absent required capability routes to fallback or blocked, never simulated capability.
- Profile changes during execution occur only at a safe checkpoint with state transfer.

## Failure Boundary

- capability hallucination
- model-brand heuristics
- unsafe light profile
- vendor lock-in
- mid-action mode switch

## Strong-Model Scaling

May skip:

- verbose capability inventory when the host contract is already machine-verified

Keep mandatory:

- risk overlay
- real capability check
- invariant preservation
- fallback

## Recommended Skill Types

- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Publish one repository skill usable by Copilot, Codex, and a tool-less chat model.

**Why it activates:** The hosts differ in filesystem, command, context, and state capabilities.

**Inputs/state:** Host manifests, task risk, and light, standard, and tool-enabled profiles are defined.

**Action:** Selects tool-enabled validation for capable agents, a document-only sequence for Copilot, and a conservative manual checklist for the tool-less model while retaining source and safety gates.

**Does not:** Assume all frontier models can run shell commands or drop integrity checks on the strongest model.

**Result/state change:** Portable behavior with explicit host-specific execution profiles.

**Companions:** ['model-size-drift-scaling', 'adapter-first-experimentation']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T4-17` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: FPMS.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 10. Tier-4 / Meta-Supervisor recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 16. COPILOT / DOCUMENT-BASED IMPLEMENTATION CONSTRAINTS (historical_assistant_artifact)
