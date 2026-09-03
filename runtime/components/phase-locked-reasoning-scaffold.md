# Stage-Separated Reasoning Scaffold (`phase-locked-reasoning-scaffold@1.1.0`)

Recovered name: Phase-Locked Reasoning Scaffold

Purpose: Prevent cross-phase contamination while still allowing explicitly governed transitions between reasoning modes.

Activate when: semantic phase leakage is a risk.

Do not use when: a single atomic transformation has no phase transition; phase labels would add more complexity than the task.

Requires: none.

## Runtime mechanism

Assign each working claim to the recovered semantic phase appropriate to its status, keep phase-specific operations and admissible transformations explicit, and require a labeled transition when a claim moves from evidence or fact into interpretation, probability, or heuristic use. The exact scaffold mechanics are derived from recovered semantic phase separation; they are not directly preserved as a historical procedure.

## Procedure

1. Declare the phases needed for the task and what claim types each admits.
2. Tag inputs and intermediate claims with their current phase.
3. Within a phase, perform only operations allowed for that claim type.
4. At a transition, record the source claim, transformation, assumptions, and destination phase.
5. Before output, audit that interpretations, probabilities, and heuristics are not stated as source facts.

## Guardrails

- Mandatory even on strong models: internal claim-status separation; explicit transition warrants for consequential inference; final status audit.
- Conflict/precedence: A transition cannot increase certainty beyond its evidence without an explicit warrant; When phase-specific outputs conflict, factual and source-locked constraints take precedence and the conflict remains visible.
- Stop or fail when: phase leakage; unlabeled inference.

Full package and provenance: [`phase-locked-reasoning-scaffold`](../../upgradeables/reasoning/phase-locked-reasoning-scaffold/UPGRADEABLE.md).
