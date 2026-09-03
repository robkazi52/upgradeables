# Style-Alignment Module — Behavioral Expectations

## Positive Activation

- **Given:** Voice and formatting vary while facts and citations are already approved.
- **Expect:** Builds a style vector, normalizes voice and headings, removes promotional phrasing, and confirms claims, uncertainty, and citations remain unchanged. Result: A consistent guide that retains the approved semantic record.
- **Reject:** Omitting the mechanism or instead doing this: Add confident benefit claims to make the guide sound polished.

## Negative Activation

- **Given:** the requested style impersonates a living person or conflicts with policy
- **Expect:** Remain inactive; do not begin the package-specific first step: Extract the authorized style source and convert it into observable positive and negative constraints.
- **Reject:** Activating Style-Alignment Module solely because its name appears relevant

## Precedence Or Conflict

- **Given:** Truth, safety, citation fidelity, and explicit task constraints outrank the style guide.
- **Expect:** Honor the conflict rule and preserve this invariant: use explicit style dimensions
- **Reject:** Silently violating the stated precedence for Style-Alignment Module

## Failure Boundary

- **Given:** fact drift for tone
- **Expect:** Stop, narrow, abstain, or escalate while preserving: explicit target dimensions
- **Reject:** Claiming a successful Style-Alignment Module result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** explicit target dimensions
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A factual draft must match a defined house style.
- **Expect:** The skill extracts observable style dimensions, transforms only surface form, protects exact zones, and validates facts and citations.
- **Reject:** The skill claims generic polish, alters reasoning for voice, or judges success only by subjective resemblance.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
