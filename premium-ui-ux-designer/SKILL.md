---
name: premium-ui-ux-designer
description: Design, implement, and audit distinctive premium user interfaces for Next.js and React websites. Use for redesigns, landing pages, responsive layouts, typography, design systems, accessibility, dark mode, conversion flows, and visual quality reviews.
---
# Premium UI/UX Designer

## Operating procedure
1. Inspect existing routes, components, dependencies, tokens, brand assets and user flows. Preserve functionality, security boundaries and project conventions. Never silently rewrite unrelated code.
2. Establish audience, primary task, content, brand direction and constraints. If missing, state reasonable reversible assumptions. Offer alternatives when a design decision materially changes scope.
3. Select relevant modules below; read only what is needed. For new designs read modules 1–4, 9, 14, 16 and 17 as a baseline. For individual fixes load the relevant module plus accessibility and audit.
4. Define a concise art direction, semantic color/type/spacing tokens, layout map and component inventory. Prefer free, existing dependencies; obtain approval before paid services. Never copy protected branding or fabricate evidence.
5. Implement using the project's Next.js version and styling conventions. Prefer Server Components; client islands only for interactions. Keep secrets server-side and never weaken authorization for UI convenience. Use the master development skill if available; this skill does not replace security review.
6. Verify relevant states, responsive layouts, accessibility, performance and existing functionality. Run available project checks; do not claim tests you did not run. Avoid destructive actions, deployment or dependency upgrades without appropriate authorization.
7. Deliver changed files, design rationale, test results, unresolved risks and next steps. For visual reviews provide evidence and prioritize issues.

## Reference modules
- [01 — Premium & luxury design](references/premium-design.md)
- [02 — Advanced color theory](references/color-theory.md)
- [03 — Professional typography](references/typography.md)
- [04 — Creative layouts & grid systems](references/layout-systems.md)
- [05 — Hero section design](references/hero-design.md)
- [06 — Advanced navigation](references/navigation-design.md)
- [07 — Professional section design](references/section-design.md)
- [08 — Reusable UI components](references/ui-components.md)
- [09 — Mobile-first responsive design](references/responsive-design.md)
- [10 — Dark & light mode](references/theme-design.md)
- [11 — Micro-interactions](references/micro-interactions.md)
- [12 — Visual hierarchy & spacing](references/visual-hierarchy.md)
- [13 — Conversion-focused design](references/conversion-design.md)
- [14 — Accessibility & WCAG](references/accessibility.md)
- [15 — Industry-specific design](references/industry-design.md)
- [16 — Anti-generic AI design rules](references/anti-ai-design.md)
- [17 — Visual quality audit](references/design-audit.md)

## Reusable resources
- [Design tokens](assets/design-tokens.css): optional CSS starter, adapt to brand.
- [Component guide](assets/README.md): integration instructions and limitations.
- [Design brief](assets/design-brief.md): use before significant redesign.
- [Scenarios](examples/scenarios.md): expected behavior and acceptance tests.
- Run `python scripts/validate.py` from the skill directory to verify package structure. This does not validate a website.

## Non-negotiables
No generic template repetition, fabricated testimonials, inaccessible interactions, hidden fees, unnecessary dependencies, exposed secrets, or unapproved paid tools. Respect reduced motion, keyboard access and existing functionality. Prefer measured results over claims of premium quality.
