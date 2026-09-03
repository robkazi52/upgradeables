# Surgery Editing — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Replace a monolithic skill loader with scoped loading and a registry.

## Why this Upgradeable activates

The change alters selection, dependency resolution, package interfaces, and state migration across the repository.

## Inputs / state

Current loader contracts, package metadata, callers, tests, and rollback version are known.

## What it does

Maps every loader responsibility, designs registry adapters, migrates callers in stages, validates resolution and fallback, then removes the monolith after cutover checks.

## What it does not do

Patch conditionals into the old loader until it accidentally behaves like two architectures.

## Result / state change

One coherent loader architecture with migrated dependents and an auditable retirement.

## Interaction with companion components

['forethought-checkpoints', 'task-set-lock-in', 'regenerative-rewrite']
