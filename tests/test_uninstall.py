from promptforge.services.uninstaller import uninstall_skill


def test_import_uninstaller():
    assert callable(uninstall_skill)