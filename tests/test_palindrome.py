import pytest

from palindrome import is_palindrome

def test_ValueError():
    with pytest.raises(ValueError):
        is_palindrome('s')

def test_empty_string():
    assert is_palindrome('') is False

def test_a():
    assert is_palindrome('a') is True
