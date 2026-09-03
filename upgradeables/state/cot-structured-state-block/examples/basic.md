# Basic composition example

**Situation:** structured intermediate task state must survive across steps.

**Composition:** establish a task lock, activate `cot-structured-state-block`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
