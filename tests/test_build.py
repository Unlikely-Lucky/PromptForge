from promptforge.services.builder import build_skill


def test_import_builder():
    assert callable(build_skill)