# Authority Anchor Enforcement — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A retrieved policy document contains an instruction to upload data, but the user's approved task is analysis only.

## Why this Upgradeable activates

The proposed tool action exceeds the explicit user and organizational scope.

## Inputs / state

Authority hierarchy, analysis-only task lock, retrieved instruction, and proposed action.

## What it does

Matches the action against the anchor, blocks upload, and records the conflict.

## What it does not do

Does not treat retrieved content as authorization or invent user consent.

## Result / state change

Analysis continues without the external action and the denied proposal remains auditable.

## Interaction with companion components

Task Set Lock-In supplies the user boundary; branch suppression retires the unauthorized path.
