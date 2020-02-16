import pytest

from palindrome import is_plaindrome

def test_empty_string():
    is_plaindrome('') is False
