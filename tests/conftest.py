import pytest

from documented.untouchable import Untouchable
from tests.common import Country


@pytest.fixture
def united_states() -> Country:
    return Country(
        regions={
            'AL': 'Alabama',
            # ...
        },
    )


@pytest.fixture
def untouchable() -> Untouchable:
    return Untouchable()
