from tests.common import Country


def test_access_by_key(united_states: Country):
    """Template can access lists and dicts by index and key."""
    assert str(united_states) == (
        'Country with regions list.\n\n'
        'Example region: Alabama.'   # noqa: WPS326
    )
