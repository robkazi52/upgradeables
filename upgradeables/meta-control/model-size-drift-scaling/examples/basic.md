# Basic composition example

**Situation:** adapting a workflow across model capability levels.

**Composition:** establish a task lock, activate `model-size-drift-scaling`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
