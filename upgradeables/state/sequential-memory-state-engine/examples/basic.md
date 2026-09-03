# Sequential Memory State Engine (SMSE) — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A support case receives a user correction after an earlier automated classification.

## Why this Upgradeable activates

The new event supersedes part of current state but history must remain auditable.

## Inputs / state

Version 12, both events, timestamps, and an authority rule favoring user-confirmed account facts.

## What it does

Normalizes the correction, resolves the conflict, commits version 13, and refreshes the support-agent view.

## What it does not do

It does not delete the earlier classification or keep both values current.

## Result / state change

Current state is corrected with a traceable transition.

## Interaction with companion components

['stateblock', 'state-snapshot', 'stable-long-context']
