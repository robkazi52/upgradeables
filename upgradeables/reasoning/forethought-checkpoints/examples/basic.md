# Forethought / Checkpoints — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

Rename a production API field.

## Why this Upgradeable activates

The change can break downstream consumers and is costly to reverse after rollout.

## Inputs / state

Consumer inventory, compatibility plan, telemetry, and rollback deployment exist.

## What it does

Verifies consumer migration, stages compatibility, sets an error-rate threshold, deploys, and checks telemetry before removing the old field.

## What it does not do

Approve the rename because the local service tests pass.

## Result / state change

A gated rollout with evidence before irreversible cleanup.

## Interaction with companion components

['risk-tier-scaling', 'multi-layer-consistency']
