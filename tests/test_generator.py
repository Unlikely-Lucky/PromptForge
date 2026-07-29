from pathlib import Path

from promptforge.generators.skill import create_skill


def test_create_skill(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    template_dir = tmp_path / "templates" / "skill"
    template_dir.mkdir(parents=True)

    (template_dir / "README.md.tpl").write_text("# {name}\n", encoding="utf-8")
    (template_dir / "SKILL.md.tpl").write_text("", encoding="utf-8")
    (template_dir / "prompt.md.tpl").write_text("", encoding="utf-8")
    (template_dir / "examples.md.tpl").write_text("", encoding="utf-8")
    (template_dir / "eval.md.tpl").write_text("", encoding="utf-8")
    (template_dir / "metadata.yaml.tpl").write_text("name: {name}", encoding="utf-8")
    (template_dir / "CHANGELOG.md.tpl").write_text("", encoding="utf-8")

    # Point the generator at the temporary template directory.
    import promptforge.generators.skill as skill_module
    skill_module.TEMPLATE_DIR = template_dir

    create_skill("demo")

    skill_dir = tmp_path / "skills" / "demo"

    assert skill_dir.exists()
    assert (skill_dir / "README.md").exists()
    assert (skill_dir / "metadata.yaml").exists()