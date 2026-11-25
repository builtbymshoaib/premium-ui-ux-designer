# Module 08 — Reusable UI components

## Principles
Use native semantics first; compose small components with typed props, predictable variants and clear states. Prefer existing primitives over new dependencies.

## Implementation workflow
Inventory components before coding; separate server-rendered content from interactive client islands. Define default, hover, focus, active, disabled, loading and error behavior as applicable. Use existing accessible dialog primitives for modal interactions.

## Practical example
A shared Button handles actions; a styled Link handles navigation; a Section provides consistent spacing without enforcing a card layout.

## Acceptance criteria
No nested interactive elements; component variants use tokens; actions are accessible with keyboard and touch.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
