# Explanation Minimality Scaffold — Behavioral Expectations

## Positive Activation

- **Given:** The user needs outcome, material changes, validation, and next step—not a narration of every command.
- **Expect:** States the completed artifact, count, validation result, and source-gap caveat in a few sentences. Result: A compact handoff that remains trustworthy and actionable.
- **Reject:** Omitting the mechanism or instead doing this: Paste the full validation log or omit the source-gap caveat to stay short.

## Negative Activation

- **Given:** the user requests a tutorial or exhaustive rationale
- **Expect:** Remain inactive; do not begin the package-specific first step: Identify the reader, requested depth, decision or action, and risk tier.
- **Reject:** Activating Explanation Minimality Scaffold solely because its name appears relevant

## Precedence Or Conflict

- **Given:** User-requested detail and risk-mandated disclosure override brevity.
- **Expect:** Honor the conflict rule and preserve this invariant: lead with the outcome
- **Reject:** Silently violating the stated precedence for Explanation Minimality Scaffold

## Failure Boundary

- **Given:** terse but unactionable output
- **Expect:** Stop, narrow, abstain, or escalate while preserving: reader-and-risk calibration
- **Reject:** Claiming a successful Explanation Minimality Scaffold result past this boundary

## Strong Model Scaling

- **Given:** a capable host can compress the workflow
- **Expect:** reader-and-risk calibration
- **Reject:** dropping the mandatory invariant

## Distinctive Mechanism

- **Given:** A correct answer contains background, repeated conclusions, a necessary caveat, and one causal bridge.
- **Expect:** The skill deletes background and repetition while retaining the bridge and caveat.
- **Reject:** The skill simply applies a word limit, drops all reasoning, or claims a recovered historical algorithm.

These are provider-neutral behavioral specifications. Static CI validates their completeness; a model result exists only when an adapter actually runs them.
