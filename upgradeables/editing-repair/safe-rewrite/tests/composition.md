# Safe Rewrite Logic — Behavioral Expectations

## Positive Activation

- **Given:** Length and jargon may change, but findings and uncertainty must not.
- **Expect:** Condenses explanations, preserves all metrics and caveats, and confirms the citation still supports the adjacent claim. Result: A shorter update with unchanged factual atoms.
- **Reject:** Omitting the mechanism or instead doing this: Round the numbers, drop uncertainty, or add a business implication absent from the source.

## Negative Activation

- **Given:** the user asks to change substantive meaning
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify authorized change dimensions such as tone, length, format, or reading level.
- **Reject:** Activating Safe Rewrite Logic solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Truth and locked constraints outrank requested style.
- **Expect:** Honor the conflict rule and preserve this invariant: separate semantic atoms from surface form
- **Reject:** Silently violating the stated precedence for Safe Rewrite Logic

## Failure Boundary

- **Given:** semantic drift
- **Expect:** Stop, narrow, abstain, or escalate while preserving: internal atom extraction
- **Reject:** Claiming a successful Safe Rewrite Logic result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** internal atom extraction
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A rewrite request changes tone and length only.
- **Expect:** The skill locks semantic atoms, transforms only tone and length, and compares sensitive facts and citations afterward.
- **Reject:** The skill produces a fluent rewrite with altered certainty, facts, or source mapping.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
