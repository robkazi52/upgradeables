# Image Text Fidelity Capture — Basic Example

**Evidence label:** Illustrative modern example. It demonstrates the v0.2 operational contract and is not presented as a recovered historical chat.

## Task context

A scanned form has one partly obscured account number and visible row labels.

## Why this Upgradeable activates

Text must be captured from an image for evidence use.

## Inputs / state

The page image and a requirement for exact transcription.

## What it does

Transcribes legible digits, preserves row order, and marks the obscured digits with their location.

## What it does not do

Infer the missing digits from another identifier.

## Result / state change

A usable transcription whose uncertainty remains auditable.

## Interaction with companion components

['grounding-no-invention', 'zero-drift-zones']
