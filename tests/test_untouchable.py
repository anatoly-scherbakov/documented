import pytest

from documented.untouchable import Untouchable


@pytest.fixture
def untouchable() -> Untouchable:
    return Untouchable()


def test_call(untouchable: Untouchable):
    with pytest.raises(Exception):
        untouchable()


def test_attribute(untouchable: Untouchable):
    with pytest.raises(Exception):
        print(untouchable.attribute)


def test_index(untouchable: Untouchable):
    with pytest.raises(Exception):
        print(untouchable['attribute'])


def test_string(untouchable: Untouchable):
    with pytest.raises(Exception):
        print(untouchable)


def test_repr(untouchable: Untouchable):
    with pytest.raises(Exception):
        print(repr(untouchable))
