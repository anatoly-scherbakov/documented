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
