---
name: source-bounded-research
description: Analyze a supplied source corpus and produce cited findings; use when conclusions must remain traceable to provided sources, not for unsourced creative writing.
---

# Source-Bounded Research

Lock the research question, source boundary, deliverable, and citation style. Use
the Deep Summary or Compare-Contrast Gene when applicable; load an authorized Core
only if domain knowledge is required. Compose `task-set-lock-in@1.0.0`,
`scoped-loader@1.0.0`, `stateblock@1.0.0`, `grounding-no-invention@1.0.0`, and
`citation-fidelity@1.0.0`; add other research-recipe components only when triggered.

Capture evidence with provenance before synthesis. Separate fact, inference,
framing, and hypothesis. For each material citation, check that the cited passage
supports the attached claim. Return findings, limitations, and unresolved evidence
conflicts. Never fabricate a source, quote, or missing fact.

Tests: reject unsupported citations; stay inactive for unsourced creative writing;
preserve the research question across a long corpus; let host policy override every
component; omit optional scaffolding on a simple one-source lookup.
