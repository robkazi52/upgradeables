# Parallel QMS

Select a named validation topology without collapsing distinct QMS modes.

## Activation boundary

Activate after defining the risk and the specific validation question.

## Required and optional components

- [`parallel-qms@1.1.0`](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) — required

## Load order and critical interactions

Use the metadata `load_order`. The package chooses only supported modes and reports whether execution was actually isolated.

## Over-scaffolding boundary

Excessive when every mode runs, or when sequential self-review is labeled distributed validation.
