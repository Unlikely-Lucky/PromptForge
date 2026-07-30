from promptforge.services.info import show_skill_info


def create_metadata(path):
    path.mkdir(parents=True)

    (path / "metadata.yaml").write_text(
        """name: reply
version: 1.0.0
author: Tester
description: Test skill
license: MIT
"""
    )


def test_show_skill_info(tmp_path, capsys):
    skills = tmp_path / "skills"

    create_metadata(skills / "reply")

    show_skill_info(
        "reply",
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "Skill Information" in out
    assert "reply" in out
    assert "Tester" in out
    assert "MIT" in out


def test_missing_skill(tmp_path, capsys):
    show_skill_info(
        "missing",
        skills_dir=tmp_path / "skills",
    )

    out = capsys.readouterr().out

    assert "does not exist" in out


def test_missing_metadata(tmp_path, capsys):
    skills = tmp_path / "skills"
    (skills / "reply").mkdir(parents=True)

    show_skill_info(
        "reply",
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "metadata.yaml not found" in out


def test_invalid_metadata(tmp_path, capsys):
    skills = tmp_path / "skills"
    skill = skills / "reply"

    skill.mkdir(parents=True)

    (skill / "metadata.yaml").write_text(
        "name: [invalid"
    )

    show_skill_info(
        "reply",
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "Error reading metadata" in out