from zipfile import ZipFile

from promptforge.services.builder import build_skill


REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "prompt.md",
    "examples.md",
    "eval.md",
    "CHANGELOG.md",
]


def create_valid_skill(path):
    path.mkdir(parents=True, exist_ok=True)

    for file in REQUIRED_FILES:
        (path / file).write_text("content")

    (path / "metadata.yaml").write_text(
        """name: reply
version: 1.0.0
author: Tester
description: Test skill
license: MIT
"""
    )


def test_build_skill_creates_zip(tmp_path):
    skills = tmp_path / "skills"
    dist = tmp_path / "dist"

    create_valid_skill(skills / "reply")

    build_skill(
        "reply",
        skills_dir=skills,
        dist_dir=dist,
    )

    archive = dist / "reply-1.0.0.zip"

    assert archive.exists()

    with ZipFile(archive) as z:
        names = z.namelist()

    assert "README.md" in names
    assert "SKILL.md" in names
    assert "prompt.md" in names
    assert "metadata.yaml" in names


def test_build_missing_skill(tmp_path, capsys):
    build_skill(
        "missing",
        skills_dir=tmp_path / "skills",
        dist_dir=tmp_path / "dist",
    )

    out = capsys.readouterr().out

    assert "does not exist" in out


def test_build_rejects_missing_files(tmp_path, capsys):
    skills = tmp_path / "skills"
    skill = skills / "reply"

    skill.mkdir(parents=True)

    build_skill(
        "reply",
        skills_dir=skills,
        dist_dir=tmp_path / "dist",
    )

    out = capsys.readouterr().out

    assert "Skill is incomplete" in out


def test_build_rejects_metadata_name_mismatch(tmp_path, capsys):
    skills = tmp_path / "skills"
    skill = skills / "reply"

    create_valid_skill(skill)

    (skill / "metadata.yaml").write_text(
        """name: wrong
version: 1.0.0
author: Tester
description: Test
license: MIT
"""
    )

    build_skill(
        "reply",
        skills_dir=skills,
        dist_dir=tmp_path / "dist",
    )

    out = capsys.readouterr().out

    assert "does not match the folder name" in out