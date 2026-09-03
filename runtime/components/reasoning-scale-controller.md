# Task-Scope Reasoning Controller (`reasoning-scale-controller@1.1.0`)

Recovered name: Reasoning-Scale Controller

Purpose: Match reasoning depth and scope to the unit of work instead of applying either shallow local analysis or system-wide architecture indiscriminately.

Activate when: task complexity or risk requires depth selection.

Do not use when: a governing workflow already fixes the required scale; the unit is safety-critical and policy mandates the highest review tier.

Requires: none.

## Runtime mechanism

Route work through one controller: Subatomic for a fact, local relation, constraint, or sentence decision; Atomic for a small verified inference or action; Nano as a light intermediate structure whose detailed historical spec remains unrecovered; Micro for task-local scaffolds and dependencies; QMS for quality evaluation; Cosmic for global architecture, strategy, or long-horizon planning. Escalate when dependency span, ambiguity, irreversibility, or risk exceeds the current scale; de-escalate after the larger question is resolved.

## Procedure

1. Identify the unit of work, dependency radius, uncertainty, and consequence of error.
2. Choose the lowest scale that can represent all relevant dependencies.
3. Execute only the operations appropriate to that scale.
4. Escalate one or more levels when local reasoning exposes unresolved cross-unit dependencies, competing quality dimensions, or global architecture effects.
5. After the higher-scale decision, return local implementation to the smallest adequate scale and record the boundary.

## Guardrails

- Mandatory even on strong models: smallest-adequate-scope selection; explicit escalation signals; global-to-local decomposition.
- Conflict/precedence: Risk-mandated review overrides the desire to stay at a cheaper scale; Cosmic conclusions must be decomposed back into verifiable local units before execution.
- Stop or fail when: scale theater; chronic overthinking.

Full package and provenance: [`reasoning-scale-controller`](../../upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md).
