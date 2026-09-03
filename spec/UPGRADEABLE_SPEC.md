# Upgradeable Specification

An Upgradeable is a versioned, reusable behavioral, reasoning, state, retrieval,
validation, editing, orchestration, or control primitive. It is not automatically
a standalone Skill. Implementations may use a Skill component, mode, validator,
state schema/manager, reference, deterministic script, orchestrator, bundle, or
archival record.

A modern Upgradeable is selectively loadable, activates under identifiable
conditions, performs a bounded transformation or control function through a
defined interface, and returns a predictable result to the host OS. A historical
item may remain preserved even when it does not meet this modern normalization
test; new contributions normally must meet it or become a mode, recipe, bundle,
profile, reference, or implementation detail.

## Functional taxonomy

`framing-intake`, `state`, `context-retrieval`, `planning-reasoning`, `truth-grounding`, `validation`, `drift-control`, `editing-repair`, `output`, `orchestration`, `meta-control`, `persistence`.

## Activation and lifecycle

Activation classes are `U0-foundational`, `U1-common-conditional`,
`U2-specialized`, `U3-high-risk-expensive`, and `U4-meta-architecture`.
Lifecycle values are `historical`, `unresolved`, `experimental`, `candidate`,
`stable`, `core`, and `deprecated`. Historical recovery status is a separate axis.

## Required contract

Metadata declares identity/version, registry generation, aliases/provenance,
recovery/lifecycle, tiers, functional and activation classes, forms, purpose,
triggers and non-triggers, inputs/outputs, dependencies and companions,
counterbalances/redundancy/conflicts, failure boundary, model scaling, and package
path. Documentation adds explicit mechanism, procedure, always/never rules,
precedence, examples, and behavioral/composition tests.

Unresolved records are archival-only and must contain no invented procedure.
Validators may approve, reject, score, veto, request repair, or abstain; they may
not manufacture supporting facts.
