from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from validate import validate, ROOT
validate()
out = ROOT.parent / (ROOT.name + ".zip")
with ZipFile(out, "w", ZIP_DEFLATED) as z:
    for f in sorted(ROOT.rglob("*")):
        if f.is_file() and not any(x in {".git", "__pycache__", "node_modules"} for x in f.relative_to(ROOT).parts) and not f.name.startswith(".env") and f.suffix not in {".zip", ".pyc"}:
            assert not f.is_symlink(), f
            z.write(f, ROOT.name + "/" + f.relative_to(ROOT).as_posix())
with ZipFile(out) as z:
    assert z.testzip() is None
    assert ROOT.name + "/SKILL.md" in z.namelist()
    print(f"PASS: {len(z.namelist())} files; {out}")
