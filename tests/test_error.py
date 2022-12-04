import dataclasses

import pytest

from documented import DocumentedError


class NotAWizard(DocumentedError):
    """{self.name}, sorry to say that you are not a wizard."""

    def __init__(self, name: str):
        """This is not a dataclass and requires a constructor."""
        self.name = name


@dataclasses.dataclass
class YouHaveLiedToMe(DocumentedError):
    """If I were you, {self.username}, I'd sue my face for slander."""

    username: str


class FailingError(DocumentedError):
    """This error cannot be {self.rendered} :("""  # noqa: D400


def test_plain_inheritance():
    """Just inherit your class from DocumentedError to get all the perks."""
    with pytest.raises(NotAWizard) as err:
        raise NotAWizard(name='Rincewind')

    assert str(err.value) == (  # noqa: WPS441
        'Rincewind, sorry to say that you are not a wizard.'
    )


def test_dataclass():
    """If exception is a dataclass, constructor is provided for you."""
    with pytest.raises(YouHaveLiedToMe) as err:
        raise YouHaveLiedToMe(username='Rincewind')

    assert str(err.value) == (  # noqa: WPS441
        "If I were you, Rincewind, I'd sue my face for slander."
    )


def test_rendering_failure():
    """Docstring template of this particular class is invalid."""
    with pytest.raises(FailingError) as err:
        raise FailingError()

    with pytest.raises(AttributeError):  # noqa: WPS441
        str(err.value)  # noqa: WPS441
