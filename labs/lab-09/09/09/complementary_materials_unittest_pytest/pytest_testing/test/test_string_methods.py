# Based on on: https://docs.python.org/3/library/unittest.html
import pytest


def test_upper():
    assert 'foo'.upper() == 'FOO'


def test_isupper():
    assert 'FOO'.isupper() == True
    assert 'Foo'.isupper() == False


def test_split():
    s = 'hello world'
    assert s.split() == ['hello', 'world']
    # check that s.split fails when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)
