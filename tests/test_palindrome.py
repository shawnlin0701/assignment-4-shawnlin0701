import pytest

from palindrome import is_palindrome

def test_ValueError():
    with pytest.raises(ValueError):
        is_palindrome('(a)')

def test_empty_string():
    assert is_palindrome('') is False

def test_a():
    assert is_palindrome('a') is True

def test_bb():
    assert is_palindrome('bb') is True
