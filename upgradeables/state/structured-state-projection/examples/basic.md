# Basic composition example

**Situation:** a component needs a bounded state view.

**Composition:** establish a task lock, activate `structured-state-projection`, preserve
explicit state and evidence boundaries, then pass the result through the
workflow's applicable validator.

**Expected:** the component performs only its documented purpose and reports
uncertainty or failure instead of manufacturing missing support.
