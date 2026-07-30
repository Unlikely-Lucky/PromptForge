from zipfile import ZipFile

from promptforge.services.installer import install_skill


REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "prompt.md",
    "examples.md",
    "eval.md",
    "CHANGELOG.md",
]


def create_package(zip_path):
    from pathlib import Path
    import tempfile

    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)

        for file in REQUIRED_FILES:
            (temp / file).write_text("content")

        (temp / "metadata.yaml").write_text(
            """name: reply
version: 1.0.0
author: Tester
description: Test
license: MIT
"""
        )

        with ZipFile(zip_path, "w") as z:
            for file in temp.iterdir():
                z.write(file, arcname=file.name)


def test_install_valid_package(tmp_path):
    package = tmp_path / "reply.zip"

    create_package(package)

    skills = tmp_path / "skills"

    install_skill(
        str(package),
        skills_dir=skills,
    )

    assert (skills / "reply").exists()
    assert (skills / "reply" / "metadata.yaml").exists()


def test_install_missing_zip(tmp_path, capsys):
    install_skill(
        str(tmp_path / "missing.zip"),
        skills_dir=tmp_path / "skills",
    )

    out = capsys.readouterr().out

    assert "does not exist" in out


def test_install_rejects_non_zip(tmp_path, capsys):
    file = tmp_path / "demo.txt"
    file.write_text("hello")

    install_skill(
        str(file),
        skills_dir=tmp_path / "skills",
    )

    out = capsys.readouterr().out

    assert "Only .zip packages are supported" in out


def test_install_rejects_duplicate(tmp_path, capsys):
    package = tmp_path / "reply.zip"

    create_package(package)

    skills = tmp_path / "skills"
    (skills / "reply").mkdir(parents=True)

    install_skill(
        str(package),
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "already installed" in out