from promptforge.services.info import show_skill_info


def test_import_info():
    assert callable(show_skill_info)