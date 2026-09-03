# State Routing Bus

## Summary

Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs.

## Purpose

Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs.

## Problem Solved

Modules lose context or invent secret coordination when no typed, visible path carries only the state each receiver is authorized to consume.

## Where It Fits in the OS

Roles: state transport, module handoff. Pipeline stages: post-module emission, inter-module routing, handoff verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-agent workflows
- modular Skills
- cross-process continuation

## When Not to Use

- all work occurs inside one uninterrupted component
- the host provides no real file, message, context, or structured-state handoff

## Scope

Canonical package: `state-routing-bus@1.1.0`. ID: `A-02`. Functional classes: state, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires multiple components exchange state.

## Non-Triggers

- all work occurs inside one uninterrupted component
- the host provides no real file, message, context, or structured-state handoff

## Inputs / Required State

- typed source state and provenance
- sender/receiver interface and permissions
- available host transport

## Outputs / Produced State

- delivered bounded state envelope
- acknowledgement or explicit handoff failure

## Mechanism

Represent the handoff as a typed envelope containing sender, receiver, schema version, authority, provenance, payload, and unresolved status. Validate the envelope and receiver permissions, transmit it through an actual host mechanism such as context, file, message, or database, then require acknowledgement. No latent pointer or hidden channel is assumed.

## Procedure

1. Define the sender, receiver, state schema, and permitted payload fields.
2. Package decisions, evidence pointers, module outputs, provenance, and unresolved items in a bounded envelope.
3. Validate schema, authority, size, and receiver permissions.
4. Transmit through an available explicit host channel and record delivery status.
5. Require acknowledgement or fail with a recoverable handoff record.

## Always-Do Rules

- Preserve the defining invariant: explicit payload, provenance, receiver boundary, and delivery status.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- claiming hidden shared memory or passing an unbounded context dump
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `stateblock`

Provides the structured state fields carried by the bus.

### `state-snapshot`

Compresses continuation state when the full live StateBlock should not move.

## Compatible Upgradeables

- `stateblock` — Provides the structured state fields carried by the bus.
- `state-snapshot` — Compresses continuation state when the full live StateBlock should not move.

## Counterbalancing Upgradeables

### `scoped-loader`

Limits what the receiver loads from the delivered state.

## Potential Redundancy

### `external-state-automation`

External State persists state in storage; the bus routes state between modules and may use that storage as one transport.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If no real host-supported handoff channel exists, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- no real host-supported handoff channel exists
- payload schema, authority, provenance, or receiver acknowledgement fails

## Strong-Model Scaling

May skip:

- transport envelopes when components share one already typed local state object

Keep mandatory:

- explicit payload, provenance, receiver boundary, and delivery status

## Recommended Skill Types

- multi-agent workflows
- modular Skills
- cross-process continuation

## Example Composition

**Task context:** A research worker hands verified evidence to a separate report writer.

**Why it activates:** The writer needs decisions and source pointers but not the worker's full context.

**Inputs/state:** Sender/receiver IDs, schema, evidence pointers, decisions, unresolved questions, and message channel.

**Action:** Validates and sends a bounded envelope, then records the writer's acknowledgement.

**Does not:** Does not claim secret shared memory or transfer private reasoning.

**Result/state change:** The writer receives traceable state or the workflow reports a handoff failure.

**Companions:** StateBlock structures payload; Scoped Loader limits receiver context.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `A-02` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Teleport Bus.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — A-02. Teleport Bus (current_consolidated_catalog)
