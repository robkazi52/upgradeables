# Future-Proof Mode Selector — Behavioral Expectations

## Positive Activation

- **Given:** The hosts differ in filesystem, command, context, and state capabilities.
- **Expect:** Portable behavior with explicit host-specific execution profiles.
- **Reject:** remaining inactive despite a satisfied trigger

## Negative Activation

- **Given:** the host and task profile are fixed
- **Expect:** the component stays inactive and adds no scaffolding
- **Reject:** activating solely because the name appears relevant

## Precedence Or Conflict

- **Given:** Task-risk requirements override host convenience.
- **Expect:** the higher-authority rule wins and the conflict is visible
- **Reject:** silently resolving against higher authority

## Failure Boundary

- **Given:** capability hallucination
- **Expect:** the component stops, abstains, narrows, or escalates as documented
- **Reject:** manufacturing a successful result past its failure boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** risk overlay
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** The same workflow targets hosts with different tools, state, context, and reliability.
- **Expect:** The skill probes capabilities, overlays risk, selects a named profile, and provides fallback without dropping invariants.
- **Reject:** The skill merely scales controls by model size or assumes every host supports the same features.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
