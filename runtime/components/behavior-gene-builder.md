# Reusable Behavior Component Builder (`behavior-gene-builder@1.1.0`)

Recovered name: Behavior Gene Builder

Purpose: Turn repeatable behavior, logic, evidence handling, and output contracts into swappable components that compose with Cores and validators.

Activate when: a recurring task family needs reusable behavior.

Do not use when: the content is primarily domain knowledge; the behavior occurs only once.

Requires: none.

## Runtime mechanism

Extract the invariant behavior shared by a task family and encode it in the recovered Gene schema: name/version, purpose, scope, triggers, always and avoid rules, reasoning pattern, evidence handling, Core interface, output contract, and compatibility notes. Test activation and non-activation cases, conflict precedence, and behavior with representative Cores; publish the behavior separately from knowledge and loader policy.

## Procedure

1. Collect repeated successful and failed task instances and isolate the stable behavior rather than domain facts.
2. Define scope, activation conditions, and explicit non-triggers.
3. Specify always-do, never-do, reasoning pattern, evidence handling, and output contract.
4. Declare Core, validator, and other-Gene interfaces plus authority and conflict rules.
5. Test positive activation, false activation, missing-Core, and conflicting-Gene cases.

## Guardrails

- Mandatory even on strong models: behavior/Core separation; trigger contract; always/avoid rules.
- Conflict/precedence: Global truth, safety, and authorization rules outrank any Gene; A Gene may query a Core but cannot silently redefine its sourced domain facts.
- Stop or fail when: behavior-knowledge conflation; monolithic Gene.

Full package and provenance: [`behavior-gene-builder`](../../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md).
