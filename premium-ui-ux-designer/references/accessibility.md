# Module 14 — Accessibility & WCAG

## Principles
Target WCAG 2.2 AA where applicable. Automated checks are supplementary, not proof of compliance.

## Implementation workflow
Use landmarks, semantic headings, labels, alt text, visible focus, keyboard navigation and accessible error announcements. Test reflow, contrast, focus not obscured and target size. Avoid placeholder-only labels, autoplay and unnecessary ARIA.

## Practical example
Use a native details/summary disclosure for FAQs and a real label for each form field; use aria-live selectively for asynchronous status.

## Acceptance criteria
Manually test keyboard-only flow, zoom, reduced motion and at least one screen reader when available; report untested checks.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
