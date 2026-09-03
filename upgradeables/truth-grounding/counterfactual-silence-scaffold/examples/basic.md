# Basic composition example

**Situation:** factual output could be contaminated by hypothetical content.

**Composition:** establish a task lock, activate `counterfactual-silence-scaffold`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
