# Future-Proof Mode Selector — Behavioral Expectations

## Positive Activation

- **Given:** The hosts differ in filesystem, command, context, and state capabilities.
- **Expect:** Selects tool-enabled validation for capable agents, a document-only sequence for Copilot, and a conservative manual checklist for the tool-less model while retaining source and safety gates. Result: Portable behavior with explicit host-specific execution profiles.
- **Reject:** Omitting the mechanism or instead doing this: Assume all frontier models can run shell commands or drop integrity checks on the strongest model.

## Negative Activation

- **Given:** the host and task profile are fixed
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare the task's risk, state, tool, and validation requirements.
- **Reject:** Activating Future-Proof Mode Selector solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Task-risk requirements override host convenience.
- **Expect:** Honor the conflict rule and preserve this invariant: test capabilities rather than infer them from brand or model size
- **Reject:** Silently violating the stated precedence for Future-Proof Mode Selector

## Failure Boundary

- **Given:** capability hallucination
- **Expect:** Stop, narrow, abstain, or escalate while preserving: risk overlay
- **Reject:** Claiming a successful Future-Proof Mode Selector result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** risk overlay
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** The same workflow targets hosts with different tools, state, context, and reliability.
- **Expect:** The skill probes capabilities, overlays risk, selects a named profile, and provides fallback without dropping invariants.
- **Reject:** The skill merely scales controls by model size or assumes every host supports the same features.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
