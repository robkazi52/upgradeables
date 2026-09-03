# Structured Refinement Cycles — Behavioral Expectations

## Positive Activation

- **Given:** The draft has two incorrect dates, a duplicated section, and inconsistent voice.
- **Expect:** Fixes dates and citations, then removes structural duplication, then aligns voice, and finally checks all three classes. Result: A release-ready guide with traceable pass boundaries and no semantic regression.
- **Reject:** Omitting the mechanism or instead doing this: Rewrite the dated sentences for tone before establishing correct dates.

## Negative Activation

- **Given:** only one bounded defect exists
- **Expect:** Remain inactive; do not begin the package-specific first step: Inventory defects and assign each to factual, structural, stylistic, or validation class.
- **Reject:** Activating Structured Refinement Cycles solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Factual correctness outranks structural elegance and style.
- **Expect:** Honor the conflict rule and preserve this invariant: separate defect classes
- **Reject:** Silently violating the stated precedence for Structured Refinement Cycles

## Failure Boundary

- **Given:** mixed-objective drift
- **Expect:** Stop, narrow, abstain, or escalate while preserving: dependency order
- **Reject:** Claiming a successful Structured Refinement Cycles result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** dependency order
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** An artifact has factual, structural, and stylistic defects.
- **Expect:** The skill classifies them, fixes them in dependency order, locks prior-pass decisions, and validates across classes.
- **Reject:** The skill performs one blended rewrite or iterates without pass boundaries.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
