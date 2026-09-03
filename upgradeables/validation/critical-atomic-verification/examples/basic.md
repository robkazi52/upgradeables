# Critical Atomic Verification — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A release note claims a migration is backward compatible.

## Why this Upgradeable activates

One removed field or changed default would invalidate the consequential conclusion.

## Inputs / state

Compatibility claim, schema diff, supported-version contract, and tests.

## What it does

Atomizes field presence, defaults, serialization, and version handling; finds the changed default critical.

## What it does not do

Approve because most integration tests pass.

## Result / state change

The compatibility claim is blocked until the default is restored or documented as breaking.

## Interaction with companion components

['citation-fidelity', 'risk-tier-scaling', 'cross-checking-chains']
