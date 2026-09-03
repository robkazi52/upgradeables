# Micro-Repair — Behavioral Expectations

## Positive Activation

- **Given:** The defect is local and the surrounding argument is correct.
- **Expect:** Freezes both paragraphs, replaces only the overstated clause with source-supported wording, and checks both transitions and citation fit. Result: The unsupported claim is removed with no unrelated semantic change.
- **Reject:** Omitting the mechanism or instead doing this: Reframe the whole section or add new evidence claims.

## Negative Activation

- **Given:** the artifact architecture is globally wrong
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the exact failed criterion and the smallest text, field, rule, or code unit causing it.
- **Reject:** Activating Micro-Repair solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead.
- **Expect:** Honor the conflict rule and preserve this invariant: name the defect before patching
- **Reject:** Silently violating the stated precedence for Micro-Repair

## Failure Boundary

- **Given:** scope creep
- **Expect:** Stop, narrow, abstain, or escalate while preserving: smallest-fault localization
- **Reject:** Claiming a successful Micro-Repair result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** smallest-fault localization
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** One local unit fails while its neighbors pass.
- **Expect:** The skill freezes passing neighbors, changes the minimum atoms, checks boundaries, and escalates if the defect proves systemic.
- **Reject:** The skill rewrites the section for general improvement or applies repeated local patches to broken architecture.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
