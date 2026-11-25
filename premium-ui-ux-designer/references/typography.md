# Module 03 — Professional typography

## Principles
Choose a readable body family and at most one expressive display family unless the brand requires more. Use next/font with appropriate subsets or system fonts; check licensing before embedding.

## Implementation workflow
Set body at roughly 16–18px with line-height 1.5–1.7; use fluid heading sizes with clamp and a sensible maximum. Limit long prose to around 60–75 characters per line. Use actual weights, avoid excessive tracking and all-caps paragraphs.

## Practical example
Editorial pairing: Georgia-style serif headings and system sans body; technical products can use a single variable sans family with distinct weights.

## Acceptance criteria
At 200% zoom no essential text is clipped; headings follow semantic order independent of visual size.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
