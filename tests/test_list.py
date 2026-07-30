from promptforge.services.listing import list_skills


def test_list_no_skills_directory(tmp_path, capsys):
    list_skills(
        skills_dir=tmp_path / "skills",
    )

    out = capsys.readouterr().out

    assert "No skills directory found." in out


def test_list_empty_directory(tmp_path, capsys):
    skills = tmp_path / "skills"
    skills.mkdir()

    list_skills(
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "No skills found." in out


def test_list_single_skill(tmp_path, capsys):
    skills = tmp_path / "skills"
    skills.mkdir()

    (skills / "reply").mkdir()

    list_skills(
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "reply" in out
    assert "Total: 1 skill" in out


def test_list_multiple_skills(tmp_path, capsys):
    skills = tmp_path / "skills"
    skills.mkdir()

    (skills / "reply").mkdir()
    (skills / "summarize").mkdir()

    list_skills(
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "reply" in out
    assert "summarize" in out
    assert "Total: 2 skills" in out


def test_list_ignores_files(tmp_path, capsys):
    skills = tmp_path / "skills"
    skills.mkdir()

    (skills / "reply").mkdir()
    (skills / "notes.txt").write_text("hello")

    list_skills(
        skills_dir=skills,
    )

    out = capsys.readouterr().out

    assert "reply" in out
    assert "notes.txt" not in out