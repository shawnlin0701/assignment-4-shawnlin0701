import pytest

from palindrome import is_palindrome

def test_empty_string():
    assert is_palindrome('') is False
