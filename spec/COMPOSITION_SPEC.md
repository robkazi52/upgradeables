# Composition Specification

The primary value of Upgradeables is composition. Select only components whose
triggers are active, preserve authority order, declare state interfaces, and
remove redundant scaffolding.

After a recipe is selected, an `R` component is structurally required but need
not run continuously. It may stay dormant until its phase-specific trigger. If
that trigger cannot occur in the workflow, reject the recipe instead of carrying
an impossible requirement.

## Common stacks

```text
Foundation: Task lock -> Mode lock -> StateBlock -> Scoped loader
            -> Working-memory cues -> Drift suppression

Evidence: Grounding -> Activation-budget funnel -> Evidence capture/index
          -> Critical atomic verification -> Multi-truth gating
          -> Citation fidelity -> Truth priority -> QMS

Exploration: Controlled drift + Cognitive flexibility + Perspective break
             -> bounded Multiverse candidates -> QMS collapse

Repair: Detect -> Micro-repair -> CRISPR edit -> Structured refinement
        -> Regenerative rewrite -> Surgery edit

Long context: StateBlock + SMSE + WM lock + Stable context + ABF
              + Attention compression + Neuro-focus + Drift suppression
              + Coherence heartbeat + State snapshot
```

Pair Neuro-Focus with Anti-Tunnel Vision; Multiverse with QMS; CRISPR with
Invariance Stress; Controlled Drift with Grounding; Risk Scaling with Dynamic
Depth; StateBlock with SMSE; Citation Fidelity with Style Alignment; Cosmic/POWER
planning with SAFE execution; and Resonance with Domain/Mode Isolation.

A composition test must cover positive activation, negative activation,
precedence conflict, unsupported claims, long-context state, over-scaffolding,
and strong-model scaling when relevant.
