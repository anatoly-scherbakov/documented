from dataclasses import dataclass

from documented import Documented, DocumentedError


@dataclass
class PodBayDoorsStillClosed(DocumentedError):
    """
    I’m sorry, {self.user_name}.

    I’m afraid I can’t do that.
    """

    user_name: str


class OpenThePodBayDoors(Documented):
    """Open the pod bay doors please, HAL."""


print(OpenThePodBayDoors())
raise PodBayDoorsStillClosed(user_name='Dave')
