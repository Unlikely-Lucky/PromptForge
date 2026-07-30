from pathlib import Path

from promptforge.generators.skill import create_skill


def test_create_skill(tmp_path):
    # Arrange
    templates = tmp_path / "templates" / "skill"
    templates.mkdir(parents=True)

    (templates / "README.md.tpl").write_text("# {name}")
    (templates / "metadata.yaml.tpl").write_text(
        "name: {name}\nauthor: {author}"
    )
    (templates / "prompt.md.tpl").write_text("{description}")

    skills_dir = tmp_path / "skills"

    # Act
    create_skill(
        name="reply",
        description="Replies politely",
        author="Tester",
        license_name="MIT",
        skills_dir=skills_dir,
        template_dir=templates,
    )

    # Assert
    skill = skills_dir / "reply"

    assert skill.exists()
    assert (skill / "README.md").exists()
    assert (skill / "metadata.yaml").exists()
    assert (skill / "prompt.md").exists()

    assert "reply" in (skill / "README.md").read_text()
    assert "Tester" in (skill / "metadata.yaml").read_text()
    assert "Replies politely" in (skill / "prompt.md").read_text()