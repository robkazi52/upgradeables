# Behavior Gene Builder — Behavioral Expectations

## Positive Activation

- **Given:** The comparison logic and output shape recur, while the evidence and entities differ by domain.
- **Expect:** Encodes dimension selection, symmetric treatment, conflict surfacing, evidence rules, and output table contract without copying any domain facts. Result: One reusable behavior module that composes with several domain Cores.
- **Reject:** Omitting the mechanism or instead doing this: Bundle the medical and legal corpora into the Gene.

## Negative Activation

- **Given:** the content is primarily domain knowledge
- **Expect:** Remain inactive; do not begin the package-specific first step: Collect repeated successful and failed task instances and isolate the stable behavior rather than domain facts.
- **Reject:** Activating Behavior Gene Builder solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Global truth, safety, and authorization rules outrank any Gene.
- **Expect:** Honor the conflict rule and preserve this invariant: keep behavior separate from domain knowledge
- **Reject:** Silently violating the stated precedence for Behavior Gene Builder

## Failure Boundary

- **Given:** behavior-knowledge conflation
- **Expect:** Stop, narrow, abstain, or escalate while preserving: behavior/Core separation
- **Reject:** Claiming a successful Behavior Gene Builder result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** behavior/Core separation
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A recurring task needs reusable reasoning behavior and domain evidence.
- **Expect:** The skill emits a behavior-only Gene with the recovered schema and explicit Core interface.
- **Reject:** The skill emits a monolithic prompt containing both behavior rules and a domain knowledge dump.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
