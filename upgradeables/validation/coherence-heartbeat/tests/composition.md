# Global Coherence Heartbeat — Behavioral Expectations

## Positive Activation

- **Given:** Local edits can drift from the handoff while still passing narrow tests.
- **Expect:** Drift is caught before release while routine checkpoints remain cheap.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the task completes in one obvious operation
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Hard constraints and explicit user updates outrank the stored baseline.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** Escalate when a hard constraint, core objective, or accepted decision no longer matches current work.
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** event-triggered pulse after major state changes in long work
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** At a milestone the build passes, but a newly added assumption contradicts the locked user constraint.
- **Expect:** Emit repair-required and escalate despite local test success.
- **Reject:** Refresh the baseline so the contradiction disappears.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
