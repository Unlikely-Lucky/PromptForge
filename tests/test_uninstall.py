from promptforge.services.uninstaller import uninstall_skill


def test_uninstall_existing_skill(tmp_path):
    skills = tmp_path / "skills"
    skill = skills / "reply"

    skill.mkdir(parents=True)

    assert skill.exists()

    uninstall_skill(
        "reply",
        skills_dir=skills,
    )

    assert not skill.exists()


def test_uninstall_missing_skill(tmp_path, capsys):
    skills = tmp_path / "skills"

    uninstall_skill(
        "missing",
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "not installed" in out