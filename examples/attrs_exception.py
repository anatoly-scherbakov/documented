from attrs import define

from documented import DocumentedError


@define
class DeathStarHasExploded(DocumentedError):
    """
    This Death Star has exploded.

    You will have to build a new one, {self.user}
    """

    user: str


raise DeathStarHasExploded(user='Darth')
