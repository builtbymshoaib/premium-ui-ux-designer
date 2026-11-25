# Module 10 — Dark & light mode

## Principles
Use semantic CSS variables in both modes rather than inverting colors. Respect system preference by default and permit explicit overrides only if useful.

## Implementation workflow
Set color-scheme correctly, and map all surface, border, text, focus and state tokens. Integrate with the existing theme provider; if adding persisted preference, ensure initial rendering avoids flash and hydration mismatch. Test images and form controls in both modes.

## Practical example
Use muted light surfaces and near-black dark surfaces with separately tuned accent and on-accent pairs.

## Acceptance criteria
Both themes pass contrast and visual checks; theme switch is labeled and keyboard accessible; no hydration warnings.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
