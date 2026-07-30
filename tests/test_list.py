from promptforge.services.listing import list_skills


def test_import_listing():
    assert callable(list_skills)