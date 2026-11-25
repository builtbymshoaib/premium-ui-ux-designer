# Module 04 — Creative layouts & grid systems

## Principles
Use content-driven grids, deliberate whitespace and consistent alignment. Reserve asymmetry for moments that deserve emphasis; do not put every section in a bordered card.

## Implementation workflow
Define container max width and fluid gutters; use CSS grid with minmax(0,1fr), flex wrapping and intrinsic sizing. Plan mobile reading order first. Use a 12-column conceptual grid for complex desktop layouts, not a mandatory 12-column DOM.

## Practical example
A case study alternates wide image-led sections with narrow text; a pricing comparison uses a consistent grid with accessible linear reading order.

## Acceptance criteria
No unintended horizontal overflow at 320 CSS px; content order remains logical without CSS.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
