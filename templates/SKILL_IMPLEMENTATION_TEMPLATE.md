---
name: <lowercase-skill-name>
description: <what this Skill does, when it activates, and important exclusions>
---

# <Skill Name>

This frontmatter is a portable discovery seed, not a universal provider manifest.
Adapt packaging fields to the target host without changing the workflow's meaning.
The `name` must match the containing folder name.

## Task Identity and Activation Boundary

## Target Host and Compatibility

## Required Inputs and Explicit State

## Behavior Gene (optional)

## Core / References (optional)

## Selected Upgradeables

| Component | Version | Decision | Active trigger | Reason |
|---|---|---|---|---|
| `<slug>` | `<version>` | Keep / Drop | <observable condition, or n/a> | <reason> |

## Authority and Precedence

## Procedure

## Validators and Failure Handling

## Output Contract

## Strong-Model Scaling

## Provenance

Name the source recipe, registry version, component versions, and any non-registry
domain sources used by this implementation.

## Tests

Include positive activation, negative activation, conflict/authority, failure,
and composition cases appropriate to the task.

Place deep sources in `references/`, repeated deterministic operations in
`scripts/`, and only necessary output materials in `assets/`.
