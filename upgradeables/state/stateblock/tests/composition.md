# StateBlock — Behavioral Expectations

## Positive Activation

- **Given:** They need a shared current objective, source set, status, and unresolved-risk record.
- **Expect:** Creates one versioned block and gives each agent a scoped view with controlled update rights. Result: Coordination and validation use the same current task truth.
- **Reject:** Omitting the mechanism or instead doing this: It does not let each agent maintain an independent final status.

## Negative Activation

- **Given:** a trivial one-turn task needs no persistent state
- **Expect:** Remain inactive; do not begin the package-specific first step: Select only fields required to execute and verify the task.
- **Reject:** Activating StateBlock solely because its name appears relevant

## Precedence Or Conflict

- **Given:** System and explicit task authority govern locked fields; evidence updates factual fields only through their declared owners.
- **Expect:** Honor the conflict rule and preserve this invariant: maintain one canonical owner
- **Reject:** Silently violating the stated precedence for StateBlock

## Failure Boundary

- **Given:** Do not proceed on dependent actions when required state is contradictory or unknown.
- **Expect:** Stop, narrow, abstain, or escalate while preserving: single source of truth
- **Reject:** Claiming a successful StateBlock result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** single source of truth
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** Several workers need current constraints, progress, and decisions.
- **Expect:** Maintain one schema-defined, versioned canonical state with controlled projections.
- **Reject:** Rely on scattered narrative summaries or multiple competing truth records.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
