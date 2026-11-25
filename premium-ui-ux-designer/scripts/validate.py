from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
def validate():
    s = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    assert s.startswith("---\n"), "Missing frontmatter"
    _, front, body = s.split("---", 2)
    name = re.search(r"^name: (.+)$", front, re.M).group(1)
    desc = re.search(r"^description: (.+)$", front, re.M).group(1)
    assert name == ROOT.name and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64
    assert 0 < len(desc) <= 1024 and len(s.splitlines()) <= 500
    refs = list((ROOT / "references").glob("*.md"))
    assert len(refs) == 17
    for f in ROOT.rglob("*.md"):
        for link in re.findall(r"\]\(([^)]+)\)", f.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#"):
                target = (f.parent / link.split("#")[0]).resolve()
                assert target.is_relative_to(ROOT) and target.exists(), (f, link)
    assert all(f"references/{f.name}" in body for f in refs)
    assert len(list((ROOT / "assets/components").glob("*.tsx"))) == 6
    print("PASS: frontmatter, name, references, relative links, component count")
if __name__ == "__main__": validate()
