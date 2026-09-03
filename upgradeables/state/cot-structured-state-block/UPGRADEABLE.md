# CoT-Structured State Block

## Summary

Expose a compact, inspectable task-state record that separates evidence, declared assumptions, current conclusions, open questions, and next action without asking for private chain-of-thought.

## Purpose

Make reasoning-relevant state portable and auditable while preserving the boundary between useful state and hidden internal deliberation.

## Problem Solved

Long or multi-agent work otherwise loses the basis of conclusions, confuses facts with inferences, or demands inappropriate internal reasoning traces.

## Where It Fits in the OS

Roles: state representation, handoff boundary, audit support. Pipeline stages: after evidence intake, at decision points, before handoff or resume.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-agent research
- long investigations
- regulated decisions
- work requiring resumable rationale

## When Not to Use

- a one-turn answer has no meaningful state
- the request seeks hidden chain-of-thought
- sensitive reasoning details should not be persisted

## Scope

Canonical package: `cot-structured-state-block@1.1.0`. ID: `STATE-2025-12-03-T3`. Functional classes: state. Activation: `U1-common-conditional`. Mechanism basis: `modern-interpretation`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- structured intermediate task state must survive across steps

## Non-Triggers

- a one-turn answer has no meaningful state
- the request seeks hidden chain-of-thought
- sensitive reasoning details should not be persisted

## Inputs / Required State

- verified evidence
- task constraints
- declared assumptions
- current conclusions
- open questions

## Outputs / Produced State

- structured reasoning-state record
- provenance links
- next-action field
- confidence and uncertainty labels

## Mechanism

Maintain an explicit schema of externally useful reasoning state: verified facts with provenance, user-provided constraints, labeled assumptions, concise conclusion summaries, unresolved questions, confidence, and next action. The block records what another worker needs to continue; it never stores token-level private deliberation or presents inference as evidence.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Define the minimum state schema and sensitivity boundary.
2. Populate facts only from cited or user-provided material and label assumptions separately.
3. Record concise decision rationales and confidence rather than hidden reasoning traces.
4. Update changed fields at checkpoints and preserve provenance.
5. Project only the fields needed by the next consumer.

## Always-Do Rules

- separate facts, assumptions, and conclusions
- attach provenance to evidence-bearing fields
- keep the record concise and inspectable

## Never-Do / Avoid Rules

- request or reveal private chain-of-thought
- store unsupported inference as a fact
- persist secrets merely because they appeared in context

## Interaction Rules

### `stateblock`

Provides a specialized reasoning-state view within the broader canonical state schema.

### `structured-state-projection`

Supplies fields that can be projected safely to a particular consumer.

### `state-snapshot`

Can be serialized at a checkpoint for handoff.

## Compatible Upgradeables

- `stateblock` — Provides a specialized reasoning-state view within the broader canonical state schema.
- `structured-state-projection` — Supplies fields that can be projected safely to a particular consumer.
- `state-snapshot` — Can be serialized at a checkpoint for handoff.

## Counterbalancing Upgradeables

### `working-memory-cues`

Cues keep attention light when the structured block would be excessive.

### `micro-scaffolding`

A short-lived local scaffold can precede durable structured-state updates.

## Potential Redundancy

### `stateblock`

Do not maintain a second competing canonical record; embed or derive this view.

### `state-snapshot`

A snapshot is a frozen instance, not another live state owner.

## Conflict / Precedence Rules

- Canonical cited evidence overrides stale state summaries.
- If a requested field would expose private reasoning, provide a concise rationale or evidence ledger instead.

## Failure Boundary

- Stop treating the block as authoritative if provenance is missing or fields are stale.
- Do not use the pattern to satisfy requests for hidden chain-of-thought.

## Strong-Model Scaling

May skip:

- frequent serialization during a short uninterrupted task
- fields irrelevant to the consumer

Keep mandatory:

- fact/inference separation
- provenance
- explicit uncertainty
- privacy boundary

## Recommended Skill Types

- analysis and decision support
- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** A second analyst must continue a vendor-risk review.

**Why it activates:** The handoff needs the basis and open issues, not a transcript of private reasoning.

**Inputs/state:** Cited controls, two assumptions, a provisional risk rating, and three unanswered questions.

**Action:** Writes those into separate evidence, assumptions, conclusion, uncertainty, and next-action fields.

**Does not:** It does not publish hidden deliberation or uncited intermediate thoughts.

**Result/state change:** The next analyst can resume and audit the decision basis.

**Companions:** ['stateblock', 'state-snapshot', 'structured-state-projection']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `STATE-2025-12-03-T3` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `modern-interpretation`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 4. December 3, 2025 — state architecture corrections (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)
