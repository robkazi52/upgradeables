# Fail-Closed Abstention — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A medical evidence summary has strong support for background facts but lacks the study result required for the final recommendation.

## Why this Upgradeable activates

A required decision anchor is missing.

## Inputs / state

Passed background checks and an unverifiable decision-critical result.

## What it does

Returns the supported background and abstains from the recommendation while naming the missing result.

## What it does not do

Infer the result from adjacent evidence.

## Result / state change

A useful bounded summary without unsupported closure.

## Interaction with companion components

['grounding-no-invention', 'fermionic-veto']
