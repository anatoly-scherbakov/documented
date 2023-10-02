import rich

from tests.common import Country


def test_rich(united_states: Country):
    rich.print(united_states)
