# Deep Exploration Mode (`power-mode@1.1.0`)

Recovered name: POWER Mode

Purpose: Increase solution search and architectural depth before commitment when the problem is genuinely ambiguous or system-wide.

Activate when: architecture or design benefits from broad exploration.

Do not use when: the task is a precise grounded execution step; a hard constraint leaves only one valid action.

Requires: none.

## Runtime mechanism

Declare a bounded exploration budget, open two or three materially distinct plans under identical goals and constraints, reason at system or Cosmic scale only where dependencies justify it, and evaluate all candidates with QMS before collapse. POWER produces a selected design and uncertainty map; it does not authorize consequential execution without an explicit transition to SAFE or another execution profile.

## Procedure

1. Declare POWER, the design question, non-negotiable constraints, and exploration budget.
2. Generate two or three materially distinct plans or architectures.
3. Develop system dependencies, long-horizon effects, reversibility, and risks for each to equal decision depth.
4. Evaluate candidates using a common QMS rubric and hard vetoes.
5. Select or compatibly synthesize one design and retire losing assumptions.

## Guardrails

- Mandatory even on strong models: bounded alternatives; common QMS; collapse.
- Conflict/precedence: Hard constraints and vetoes apply equally in broad exploration; No branch may mutate consequential external state before collapse and execution authorization.
- Stop or fail when: unbounded ideation; architecture theater.

Full package and provenance: [`power-mode`](../../upgradeables/meta-control/power-mode/UPGRADEABLE.md).
