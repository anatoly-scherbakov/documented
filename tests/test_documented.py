import dataclasses
from typing import Dict

from documented import Documented


@dataclasses.dataclass
class Country(Documented):
    """
    Country with regions list.

    Example region: {self.regions[AL]}.
    """

    regions: Dict[str, str]


def test_access_by_key():
    """Template can access lists and dicts by index and key."""
    united_states = Country(
        regions={
            'AL': 'Alabama',
            # ...
        },
    )

    assert str(united_states) == (
        'Country with regions list.\n\n' +
        'Example region: Alabama.'
    )
