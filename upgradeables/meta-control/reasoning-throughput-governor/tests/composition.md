# Reasoning Throughput Governor — Behavioral Expectations

## Positive Activation

- **Given:** Generation can run in parallel, but source review and schema validation can become bottlenecks.
- **Expect:** Limits active package batches, keeps validation one batch behind, reduces concurrency when rework rises, and reports accepted profiles per hour. Result: Steady validated output without queue or review collapse.
- **Reject:** Omitting the mechanism or instead doing this: Launch all 200 at once or count unvalidated drafts as throughput.

## Negative Activation

- **Given:** the task is one atomic operation
- **Expect:** Remain inactive; do not begin the package-specific first step: Map the workflow stages, dependencies, and mandatory serial gates.
- **Reject:** Activating Reasoning Throughput Governor solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Mandatory serial dependencies and vetoes override concurrency goals.
- **Expect:** Honor the conflict rule and preserve this invariant: measure useful completion rather than raw output volume
- **Reject:** Silently violating the stated precedence for Reasoning Throughput Governor

## Failure Boundary

- **Given:** raw-volume optimization
- **Expect:** Stop, narrow, abstain, or escalate while preserving: validation backpressure
- **Reject:** Claiming a successful Reasoning Throughput Governor result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** validation backpressure
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A workflow has an adequate total budget and depth plan but generation outpaces validation.
- **Expect:** The skill adjusts work in progress, batching, concurrency, and backpressure using completion and rework signals.
- **Reject:** The skill merely lowers total reasoning budget or reallocates depth among task regions.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
