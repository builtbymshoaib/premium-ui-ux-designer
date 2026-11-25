# Module 17 — Visual quality audit

## Principles
Review actual rendered pages rather than claiming quality from source alone. Separate observed findings from predictions and untested items.

## Implementation workflow
Capture screenshots at mobile and desktop sizes, light/dark where supported, and loading/empty/error states. Check hierarchy, consistency, keyboard, contrast, overflow and LCP/CLS risks. Record severity, evidence, proposed fix and retest status.

## Practical example
P0 blocked checkout or inaccessible core action; P1 clipped mobile content or contrast failure; P2 inconsistent spacing; P3 cosmetic refinements.

## Acceptance criteria
No unresolved P0/P1 issues for release unless explicitly accepted with documented mitigation; report tests not run and why.

## Review checklist
- [ ] Inspect existing implementation and preserve working behavior.
- [ ] Apply the implementation workflow to the actual content and constraints.
- [ ] Verify the acceptance criteria with rendered evidence where possible.
- [ ] Record exceptions, risks and untested conditions.
