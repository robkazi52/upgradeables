from example_api import normalize_name


def test_normalize_name_preserves_public_default():
    assert normalize_name(" Ada ") == "Ada"
