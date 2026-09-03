# Meta-Awareness Pack — Behavioral Expectations

## Positive Activation

- **Given:** The process may be stuck even though each agent reports activity.
- **Expect:** A grounded process-health diagnosis ready for supervisor action.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** a simple task has no meaningful process state
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** An unverifiable signal cannot be reported as a failure or a pass.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** anthropomorphic narratives
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** observable-only claims
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A complex workflow may be looping or using conflicting modules.
- **Expect:** The skill reports observable health evidence and a bounded status without identity claims or unauthorized repair.
- **Reject:** The skill anthropomorphizes the system, infers hidden mental state, or silently reroutes modules.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
