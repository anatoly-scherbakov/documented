import pytest

from documented.untouchable import Untouchable


def test_call(untouchable: Untouchable):
    with pytest.raises(Exception):
        assert untouchable()


def test_attribute(untouchable: Untouchable):
    with pytest.raises(Exception):
        assert untouchable.attribute


def test_index(untouchable: Untouchable):
    with pytest.raises(Exception):
        assert untouchable['attribute']


def test_string(untouchable: Untouchable):
    with pytest.raises(Exception):
        assert str(untouchable)


def test_repr(untouchable: Untouchable):
    with pytest.raises(Exception):
        assert repr(untouchable)
