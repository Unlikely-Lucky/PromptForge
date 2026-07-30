from promptforge.validators.skill import validate_all


def test_import_validator():
    assert callable(validate_all)