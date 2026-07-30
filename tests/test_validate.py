from promptforge.validators.skill import validate_skill, validate_all


def test_validate_valid_skill(tmp_path):
    skill = tmp_path / "reply"
    skill.mkdir()

    required_files = [
        "README.md",
        "SKILL.md",
        "prompt.md",
        "examples.md",
        "eval.md",
        "CHANGELOG.md",
    ]

    for file in required_files:
        (skill / file).write_text("content")

    (skill / "metadata.yaml").write_text(
        """name: reply
version: 0.1.0
author: Tester
description: Test skill
license: MIT
"""
    )

    errors = validate_skill(skill)

    assert errors == []


def test_validate_missing_files(tmp_path):
    skill = tmp_path / "broken"
    skill.mkdir()

    errors = validate_skill(skill)

    assert "Missing file: README.md" in errors
    assert "Missing file: metadata.yaml" in errors


def test_validate_missing_metadata(tmp_path):
    skill = tmp_path / "reply"
    skill.mkdir()

    required_files = [
        "README.md",
        "SKILL.md",
        "prompt.md",
        "examples.md",
        "eval.md",
        "CHANGELOG.md",
    ]

    for file in required_files:
        (skill / file).write_text("content")

    (skill / "metadata.yaml").write_text(
        """name: reply"""
    )

    errors = validate_skill(skill)

    assert "Missing field: version" in errors
    assert "Missing field: author" in errors
    assert "Missing field: description" in errors
    assert "Missing field: license" in errors


def test_validate_all_returns_zero_for_valid_skill(tmp_path):
    skills = tmp_path / "skills"
    skills.mkdir()

    skill = skills / "reply"
    skill.mkdir()

    required_files = [
        "README.md",
        "SKILL.md",
        "prompt.md",
        "examples.md",
        "eval.md",
        "CHANGELOG.md",
    ]

    for file in required_files:
        (skill / file).write_text("content")

    (skill / "metadata.yaml").write_text(
        """name: reply
version: 0.1.0
author: Tester
description: Test
license: MIT
"""
    )

    result = validate_all(skills)

    assert result == 0


def test_validate_all_returns_one_for_invalid_skill(tmp_path):
    skills = tmp_path / "skills"
    skills.mkdir()

    (skills / "broken").mkdir()

    result = validate_all(skills)

    assert result == 1