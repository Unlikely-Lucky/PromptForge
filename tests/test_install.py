from promptforge.services.installer import install_skill


def test_import_installer():
    assert callable(install_skill)