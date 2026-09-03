# Progressive Mode Shaping — Behavioral Expectations

## Positive Activation

- **Given:** Exploration is useful early but must not persist into engineering execution.
- **Expect:** Narrows from ideation to comparison to one plan, locking decisions at each transition. Result: Engineering receives one precise specification with traceable retired alternatives.
- **Reject:** Omitting the mechanism or instead doing this: Does not keep rejected features active or force a premature choice without comparison.

## Negative Activation

- **Given:** the task is purely exploratory and requires no commitment
- **Expect:** Remain inactive; do not begin the package-specific first step: Declare the initial exploration boundary and the decisions that must eventually lock.
- **Reject:** Activating Progressive Mode Shaping solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Host, system, domain, and explicit user authority take precedence over this component.
- **Expect:** Honor the conflict rule and preserve this invariant: Preserve the defining invariant: evidence-backed narrowing and retirement of losing branches before execution.
- **Reject:** Silently violating the stated precedence for Progressive Mode Shaping

## Failure Boundary

- **Given:** transition criteria are absent or accepted decisions cannot be distinguished from open options
- **Expect:** Stop, narrow, abstain, or escalate while preserving: evidence-backed narrowing and retirement of losing branches before execution
- **Reject:** Claiming a successful Progressive Mode Shaping result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** evidence-backed narrowing and retirement of losing branches before execution
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** a workflow must turn broad exploration into one executable plan over several phases
- **Expect:** allowed breadth shrinks as decisions lock and losing branches are retired
- **Reject:** keeping every alternative active through execution or narrowing without evidence

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
