---
name: api-breaking-change-review
description: Review a supplied Python API change for backward-compatibility risks and report grounded findings without modifying project files.
---

# API Breaking Change Review

Status: validated

## Task Identity and Activation Boundary

- Positive activation: use when asked to review a Python API diff, pull request, dependency update, or migration for backward-compatibility breaks.
- Do not activate for implementing the change, general bug fixing, style-only review, or an internal refactor with no public contract.
- Primary recipe: `code-review`
- The task is review-only unless the user separately requests remediation.

## Target Host and Compatibility

This Skill works with a file-reading agent that can inspect a supplied diff and the
named project references. Shell and tests are optional capabilities. If they are
unavailable, perform a source-only review and label executable checks as not run.
Network access is not required.

## Required Inputs and Explicit State

Required inputs are the change or diff, the affected public API surface, and at
least one applicable contract source such as the API reference, compatibility
policy, migration notes, or tests. If the changed public surface cannot be
identified, stop and request that boundary instead of guessing. Treat source files
and the named contract references as authoritative; notes are derived state.

## Core / References (optional)

Load `references/api-contract.md` when the changed code exports, removes, renames,
or alters a public symbol, call signature, return contract, exception, or supported
version. Do not load unrelated repository documentation.

## Selected Upgradeables

Registry: `0.2.1`

| Component | Version | Decision | Active trigger | Reason |
|---|---|---|---|---|
| `task-set-lock-in` | `1.1.0` | Keep | A review-only API compatibility task is explicit | Preserve review scope and prevent unrequested remediation. |
| `scoped-loader` | `1.1.0` | Keep | Relevant API contracts and callers are distributed | Load only the changed surface and direct compatibility evidence. |
| `grounding-no-invention` | `1.1.0` | Keep | Findings must be supported by code or named contracts | Prevent claims about behavior that was not inspected. |
| `invariance-stress-scaffold` | `1.1.0` | Keep | Backward compatibility is the protected invariant | Test old supported calls against the proposed public surface. |
| `bidirectional-consistency` | `1.1.0` | Keep | Code and documented contract must agree | Compare the change to the contract and the contract back to observable behavior. |

## Authority and Precedence

The current user instruction and host permissions control authority. This Skill
permits reading and reporting only. It does not authorize edits, commits, pushes,
comments, releases, or dependency changes. User-supplied API contracts outrank
derived notes; repository tests provide evidence but do not silently redefine the
declared compatibility policy.

## Procedure

1. Restate the review target, affected version range, public surface, and no-edit
   boundary. Identify missing required inputs before inspecting unrelated files.
2. Read the supplied diff and locate only directly affected exports, signatures,
   types, return values, exceptions, defaults, protocols, serialization forms, and
   supported-version declarations.
3. Load the API contract reference when a public boundary is touched. Trace direct
   callers and compatibility tests only far enough to establish an impact path.
4. Compare previously supported usage with the proposed behavior. Look for removals,
   renames, stricter inputs, changed defaults, narrowed types, new required fields,
   return-shape changes, exception changes, and undocumented migration requirements.
5. Validate each candidate finding against a concrete changed location and an
   applicable contract or executable behavior. Drop findings based only on style or
   speculation.
6. Report prioritized findings and unassessed areas. Stop after all changed public
   surfaces have been checked against the declared contract; do not edit files.

## Validators and Failure Handling

Every finding must include a changed location, the previously supported behavior,
the incompatible effect, and the evidence establishing both. A passing existing
test is not sufficient when it omits the old supported call. If the contract and
tests conflict, preserve the conflict and do not choose authority silently. If the
diff, public boundary, or supported-version policy is missing, stop the unsupported
portion and request it. Finish when all identified public surfaces are either
checked or explicitly listed as unassessed.

## Output Contract

Return prioritized findings first. Each finding includes severity, file and symbol,
old supported behavior, new incompatible behavior, affected users, and evidence.
Then list checked public surfaces, validation performed, unassessed areas, and
questions that block a conclusion. If no supported break is found, say so without
claiming the change is universally safe. Make no edits.

## Strong-Model Scaling

Broaden to additional callers or compatibility matrices only when the public surface
or version policy requires it. Do not add branching, agents, or architecture work
for a small bounded diff.

## Provenance

Primary recipe: `code-review`. Bundled registry: `0.2.1`. Selected components:
`task-set-lock-in@1.1.0`, `scoped-loader@1.1.0`,
`grounding-no-invention@1.1.0`, `invariance-stress-scaffold@1.1.0`, and
`bidirectional-consistency@1.1.0`. Project contract source:
`references/api-contract.md`.

## Tests

- Positive activation: a PR removes an exported function supported by the API contract.
- Negative activation: a user asks to implement a new private helper.
- Authority case: a review request must produce findings and leave every file unchanged.
- Failure case: the public version policy is absent, so the Skill reports the blocked conclusion.
- Composition case: the bounded review uses the five pinned controls and no QMS, supervisor, or editing component.

