# Premium UI/UX Designer
Version 1.0.0 — reusable Claude Agent Skill for Next.js/React visual design and accessibility. Includes 17 modules, six component starters, design tokens, briefs, scenarios and validation scripts. Complements a master development skill; it is not a security or accessibility certification.

## Claude.ai installation
Download the ZIP containing the `premium-ui-ux-designer/` folder at archive root. In Claude, enable file creation/code execution if required, then open Customize > Skills and use the create/upload skill option. Upload ZIP and enable it. Availability may depend on plan and organization permissions. See https://support.claude.com/en/articles/12512198-how-to-create-custom-skills and https://support.claude.com/en/articles/12512180-use-skills-in-claude.

## Claude Code (Windows PowerShell)
Publish this extracted directory as a GitHub repository first, then run:
```powershell
New-Item -ItemType Directory -Force "$HOME/.claude/skills"
git clone https://github.com/YOUR_USERNAME/premium-ui-ux-designer.git "$HOME/.claude/skills/premium-ui-ux-designer"
```
For a project-local install, place the skill folder in `.claude/skills/`. Invoke `/premium-ui-ux-designer` or request it by name. See https://code.claude.com/docs/en/skills.

## Publish to GitHub
Create an empty repository named `premium-ui-ux-designer`. From the extracted skill folder:
```bash
git init
git add .
git commit -m "Initial premium UI UX skill"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/premium-ui-ux-designer.git
git push -u origin main
```
Replace YOUR_USERNAME. Choose repository visibility and a license before public distribution; no license selected by default.

## Use
“Use premium-ui-ux-designer to redesign my Next.js homepage. Preserve existing functionality, propose an art direction, implement responsive accessible components, and report actual validation results. No paid tools without approval.”

## Maintenance
Python 3 standard library only for scripts. Run `python scripts/validate.py` and `python scripts/package.py` from the skill folder. Review references as framework and accessibility standards evolve. Component examples require integration testing in a real project. Live Claude installation and website browser tests are not performed by package validation.

## Further references
- https://agentskills.io/specification
- https://nextjs.org/docs
- https://www.w3.org/TR/WCAG22/
- https://web.dev/vitals/
