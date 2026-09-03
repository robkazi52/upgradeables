# Meta-Awareness Pack — Behavioral Expectations

## Positive Activation

- **Given:** The process may be stuck even though each agent reports activity.
- **Expect:** Detects unchanged state and repeated action signatures, emits repair-required with evidence, and routes the finding to Meta-Supervisor. Result: A grounded process-health diagnosis ready for supervisor action.
- **Reject:** Omitting the mechanism or instead doing this: Claim the agents are confused or reset their work directly.

## Negative Activation

- **Given:** a simple task has no meaningful process state
- **Expect:** Remain inactive; do not begin the package-specific first step: Read declared mode, locked goal, state version, active modules, and expected next transition.
- **Reject:** Activating Meta-Awareness Pack solely because its name appears relevant

## Precedence Or Conflict

- **Given:** An unverifiable signal cannot be reported as a failure or a pass.
- **Expect:** Honor the conflict rule and preserve this invariant: limit claims to observable process state
- **Reject:** Silently violating the stated precedence for Meta-Awareness Pack

## Failure Boundary

- **Given:** anthropomorphic narratives
- **Expect:** Stop, narrow, abstain, or escalate while preserving: observable-only claims
- **Reject:** Claiming a successful Meta-Awareness Pack result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** observable-only claims
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A complex workflow may be looping or using conflicting modules.
- **Expect:** The skill reports observable health evidence and a bounded status without identity claims or unauthorized repair.
- **Reject:** The skill anthropomorphizes the system, infers hidden mental state, or silently reroutes modules.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
