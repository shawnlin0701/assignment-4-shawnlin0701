import pytest

from palindrome import is_palindrome

def test_ValueError():
    with pytest.raises(ValueError):
        is_palindrome(int)

def test_empty_string():
    assert is_palindrome("") is False

def test_a():
    assert is_palindrome("a") is True

def test_bb():
    assert is_palindrome("bb") is True

def test_abc():
    assert is_palindrome("abc") is False

def test_laval():
    assert is_palindrome("laval") is True

def test_toronto():
    assert is_palindrome("toronto") is False

def test_Able():
    assert is_palindrome("Able was I ere I saw Elba") is True
