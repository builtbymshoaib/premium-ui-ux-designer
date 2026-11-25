# Module 02 — Advanced color theory

## Principles
Separate primitive colors from semantic roles: canvas, surface, text, muted, border, accent, on-accent, danger and focus. Use a restrained accent distribution; never rely on color alone for meaning.

## Implementation workflow
Start with a neutral ramp and one brand hue. Test actual foreground/background combinations in both themes, including hover, disabled and error states. Keep imagery and gradients away from text unless a tested overlay supports contrast.

## Practical example
For hospitality use warm ivory and deep forest; for enterprise use cool neutrals and navy. Do not force either onto an established brand.

## Acceptance criteria
Normal text contrast at least 4.5:1, large text 3:1, relevant non-text UI 3:1; verify computed colors rather than palette swatches alone.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
