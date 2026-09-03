# Reasoning Efficiency Controller (`reasoning-throughput-governor@1.1.0`)

Recovered name: Reasoning Throughput Governor

Purpose: Maximize useful completed work per unit time while respecting the Cognitive Governor's budget and every mandatory validation barrier.

Activate when: latency, breadth, and validation compete.

Do not use when: the task is one atomic operation; safety protocol requires a strictly serial sequence.

Requires: none.

## Runtime mechanism

Treat planning, generation, evidence acquisition, and validation as a bounded work queue. Set limits on active branches, batch size, and how far unchecked output may accumulate; observe completion rate, rework, validator backlog, and error rate, then add backpressure, reduce breadth, or rebalance stages. RTG governs how work flows under a budget; Cognitive Governor sets total spend and DDA sets depth per region.

## Procedure

1. Map the workflow stages, dependencies, and mandatory serial gates.
2. Set initial work-in-progress, branch, batch, and unchecked-output limits.
3. Measure useful completions, latency, rework, error rate, and validator backlog.
4. Increase concurrency or batch size only where independent work exists and checks keep pace.
5. Apply backpressure or narrow breadth when validation lags or rework rises.

## Guardrails

- Mandatory even on strong models: validation backpressure; dependency-aware concurrency; useful-completion metric.
- Conflict/precedence: Mandatory serial dependencies and vetoes override concurrency goals; When validation backlog grows, production slows before checks are weakened.
- Stop or fail when: raw-volume optimization; validator starvation.

Full package and provenance: [`reasoning-throughput-governor`](../../upgradeables/meta-control/reasoning-throughput-governor/UPGRADEABLE.md).
