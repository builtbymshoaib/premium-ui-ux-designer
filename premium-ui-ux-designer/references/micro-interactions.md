# Module 11 — Micro-interactions

## Principles
Motion should explain state change, hierarchy or navigation; it is never a prerequisite for reading or using the site.

## Implementation workflow
Prefer CSS for simple transitions; add Motion or GSAP only for justified complexity. Animate transform and opacity where appropriate; avoid layout thrashing, scroll hijacking and infinite decorative movement. Respect prefers-reduced-motion and provide pause controls where required.

## Practical example
A button changes background on hover and focus; a disclosure expands without delaying access to its contents.

## Acceptance criteria
Reduced-motion users receive equivalent functionality; animations do not cause layout shifts or block input.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
