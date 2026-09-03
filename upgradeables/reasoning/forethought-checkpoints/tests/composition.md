# Forethought / Checkpoints — Behavioral Expectations

## Positive Activation

- **Given:** The change can break downstream consumers and is costly to reverse after rollout.
- **Expect:** Verifies consumer migration, stages compatibility, sets an error-rate threshold, deploys, and checks telemetry before removing the old field. Result: A gated rollout with evidence before irreversible cleanup.
- **Reject:** Omitting the mechanism or instead doing this: Approve the rename because the local service tests pass.

## Negative Activation

- **Given:** reversible low-cost local edits
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the next irreversible, high-cost, or dependency-sensitive action.
- **Reject:** Activating Forethought / Checkpoints solely because its name appears relevant

## Precedence Or Conflict

- **Given:** A failed hard prerequisite blocks commitment regardless of schedule pressure.
- **Expect:** Honor the conflict rule and preserve this invariant: tie each checkpoint to a concrete consequence
- **Reject:** Silently violating the stated precedence for Forethought / Checkpoints

## Failure Boundary

- **Given:** ritual checklists unrelated to risk
- **Expect:** Stop, narrow, abstain, or escalate while preserving: pre-commit prerequisite check for consequential actions
- **Reject:** Claiming a successful Forethought / Checkpoints result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** pre-commit prerequisite check for consequential actions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A workflow is about to perform a costly dependency-sensitive action.
- **Expect:** The skill predicts a downstream failure, checks its prerequisite and rollback, commits, then observes.
- **Reject:** The skill offers only a generic caution or performs review after the irreversible step.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
