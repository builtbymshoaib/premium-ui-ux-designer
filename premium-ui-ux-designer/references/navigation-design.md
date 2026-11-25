# Module 06 — Advanced navigation

## Principles
Use user task labels rather than internal organization names. Keep primary links limited to meaningful destinations; show the current page and provide a skip link.

## Implementation workflow
Use semantic nav and links; use a button for a disclosure menu with aria-expanded, Escape handling and visible focus. Do not assign ARIA menu roles to ordinary site navigation. Ensure sticky headers do not obscure anchor targets.

## Practical example
A restaurant includes Menu, Deals, Location and Order; a portfolio includes Work, Services and Contact.

## Acceptance criteria
All links and disclosure controls are keyboard usable; mobile navigation closes after selection; focus is not lost.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
