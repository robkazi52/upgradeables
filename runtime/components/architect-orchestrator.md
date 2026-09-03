# Modular System Design Orchestrator (`architect-orchestrator@1.1.0`)

Recovered name: Architect Orchestrator

Purpose: Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state.

Activate when: designing or refactoring a Skill, OS, framework, or workflow.

Do not use when: the task is a narrow domain execution job with no architecture decision; a single existing component already performs the complete bounded task.

Requires: none.

## Runtime mechanism

Translate the locked goal and constraints into a modular plan, select only the necessary OS layers, Genes, Cores, Upgradeables, references, and validators, then coordinate their ordered execution. After execution, run a separate critique, route localized defects to bounded repair, synthesize one result, and emit the minimum continuation state. The orchestrator owns coordination, not every domain operation.

## Procedure

1. Lock the goal, constraints, deliverable, authority, and completion criteria.
2. Decompose the architecture into modules with explicit interfaces and dependencies.
3. Select the minimum required components and resolve authority, conflict, and load order.
4. Coordinate execution or delegation while passing only explicit bounded state.
5. Critique the assembled result, apply localized repair, synthesize, and emit a compact state snapshot.

## Guardrails

- Mandatory even on strong models: explicit modular interfaces, authority resolution, independent critique, and continuation state.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If required module interfaces or authority relationships cannot be resolved, stop or escalate rather than forcing a nominal success.
- Stop or fail when: required module interfaces or authority relationships cannot be resolved; the requested work is domain execution outside the orchestrator's design scope.

Full package and provenance: [`architect-orchestrator`](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md).
