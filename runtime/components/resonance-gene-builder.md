# Cross-Module Coordination Rule Builder (`resonance-gene-builder@1.1.0`)

Recovered name: Resonance Gene Builder

Purpose: Make useful cross-module reinforcement explicit and reusable without merging modules, duplicating content, or granting hidden communication.

Activate when: the same module relationship recurs.

Do not use when: the need is a general task behavior unrelated to module coupling; the modules interact only once.

Requires: none.

## Runtime mechanism

Identify a repeated module relationship and encode a narrow coupling Gene containing activation pattern, participants, directional inputs and outputs, ordering, reinforcement rule, suppression rule, authority precedence, termination, and failure behavior. Test the coupling with one participant absent, with conflicting instructions, and with irrelevant output. Reinforcement means clearer coordination through real state or context, never repeated claims or imagined latent links.

## Procedure

1. Collect repeated cases where the same modules should coordinate and isolate the stable relationship.
2. Name participants, trigger, direction of state or evidence flow, and completion condition.
3. Specify which outputs reinforce the next module and which irrelevant or conflicting effects are suppressed.
4. Declare authority ordering, unavailable-module behavior, and conflict escalation.
5. Test normal coupling, missing participant, conflict, repetition, and termination cases.

## Guardrails

- Mandatory even on strong models: explicit interfaces; authority rule; suppression behavior.
- Conflict/precedence: Global authority ordering outranks a coupling's preferred flow; Missing participants disable or degrade the coupling explicitly rather than being hallucinated.
- Stop or fail when: implicit coupling; repetition amplification.

Full package and provenance: [`resonance-gene-builder`](../../upgradeables/meta-control/resonance-gene-builder/UPGRADEABLE.md).
