import pytest

from tests.common import Country


@pytest.fixture
def united_states() -> Country:
    return Country(
        regions={
            'AL': 'Alabama',
            # ...
        },
    )
