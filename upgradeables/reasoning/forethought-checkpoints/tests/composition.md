# Forethought / Checkpoints — Behavioral Expectations

## Positive Activation

- **Given:** The change can break downstream consumers and is costly to reverse after rollout.
- **Expect:** A gated rollout with evidence before irreversible cleanup.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** reversible low-cost local edits
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** A failed hard prerequisite blocks commitment regardless of schedule pressure.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** ritual checklists unrelated to risk
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** pre-commit prerequisite check for consequential actions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A workflow is about to perform a costly dependency-sensitive action.
- **Expect:** The skill predicts a downstream failure, checks its prerequisite and rollback, commits, then observes.
- **Reject:** The skill offers only a generic caution or performs review after the irreversible step.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
