# Structured State Projection

## Summary

Produce a read-limited, purpose-specific view of canonical state for one consumer while preserving field identity and provenance.

## Purpose

Reduce context, privacy, and authority leakage between components.

## Problem Solved

Passing the full StateBlock to every agent or tool exposes irrelevant or sensitive fields and encourages unauthorized mutation.

## Where It Fits in the OS

Roles: least-privilege state view, component boundary, context minimization. Pipeline stages: before component invocation, domain transfer, handoff, output merge.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-agent systems
- domain isolation
- sensitive workflows
- tool calls with narrow schemas

## When Not to Use

- one trusted consumer legitimately needs the whole safe state
- field dependencies are unknown
- projection could conceal a safety-critical constraint

## Scope

Canonical package: `structured-state-projection@1.1.0`. ID: `JAN26-13`. Functional classes: state, output. Activation: `U2-specialized`. Mechanism basis: `provisional`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- a component needs a bounded state view

## Non-Triggers

- one trusted consumer legitimately needs the whole safe state
- field dependencies are unknown
- projection could conceal a safety-critical constraint

## Inputs / Required State

- canonical StateBlock version
- consumer identity
- field policy
- sensitivity labels
- required constraints

## Outputs / Produced State

- versioned purpose-specific state view
- redaction record
- write-back policy

## Mechanism

A modern interpretation is to define a projection contract listing allowed fields, necessary derived values, redactions, provenance, version, and write-back rights. Materialize the view from canonical state at invocation time and merge returned deltas only through the canonical owner's validation path.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify the consumer and its minimum information need.
2. Declare included, derived, redacted, and mandatory safety fields.
3. Generate the view from an identified canonical state version.
4. Attach provenance and freshness metadata.
5. Validate any returned delta against the consumer's write rights before canonical merge.

## Always-Do Rules

- include mandatory constraints even when they are not task content
- preserve source field identity
- declare freshness/version
- validate write-back separately

## Never-Do / Avoid Rules

- copy the full state by default
- grant mutation rights through a read projection
- drop a constraint required for safe interpretation

## Interaction Rules

### `stateblock`

Is the canonical source from which projections are derived.

### `domain-mode-isolation`

Provides the controlled bridge across isolated domains.

### `scoped-loader`

Pairs resource minimization with state minimization.

## Compatible Upgradeables

- `stateblock` — Is the canonical source from which projections are derived.
- `domain-mode-isolation` — Provides the controlled bridge across isolated domains.
- `scoped-loader` — Pairs resource minimization with state minimization.

## Counterbalancing Upgradeables

### `cot-structured-state-block`

Ensures the projected reasoning-relevant view remains inspectable without exposing private deliberation.

### `clarification-gateway`

Clarifies uncertain consumer needs before aggressive field removal.

## Potential Redundancy

### `attention-compression-scaffold`

Both reduce active context; projection enforces a consumer contract, while attention compression is a temporary cognitive view.

### `state-snapshot`

A snapshot freezes a version; projection filters a version for use.

## Conflict / Precedence Rules

- Mandatory safety and authority fields override a consumer's request to omit them.
- A returned projection delta cannot overwrite fields outside declared write scope.

## Failure Boundary

- Do not project when required field dependencies or safety constraints are unknown.
- Treat this mechanism as provisional until original concept-specific documentation is recovered.

## Strong-Model Scaling

May skip:

- materializing a separate object for a simple trusted one-consumer task
- derived convenience fields

Keep mandatory:

- least privilege
- mandatory constraints
- version/provenance
- write-back validation

## Recommended Skill Types

- multi-agent systems
- domain isolation
- sensitive workflows
- tool calls with narrow schemas

## Example Composition

**Task context:** A citation checker reviews a report produced from sensitive case state.

**Why it activates:** It needs claims and source pointers, not identities or strategy notes.

**Inputs/state:** Canonical version 17 with claim, source, identity, permissions, and strategy fields.

**Action:** Projects claims, citations, relevant constraints, and version metadata with no mutation rights.

**Does not:** It does not expose identities or allow the checker to edit task authority.

**Result/state change:** Citation checking occurs with minimal disclosure and safe merge boundaries.

**Companions:** ['stateblock', 'domain-mode-isolation', 'scoped-loader']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-13` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)
