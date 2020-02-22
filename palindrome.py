"""
palindrome.py code
"""
from collections import deque

def is_palindrome(value: str):
    """
    validates strings as palindromes.
    """
    if isinstance(value, str) is False:
        raise ValueError

    lowercase_value = list(map(lambda value: value.lower(), value))
    deque_list = deque(lowercase_value)
    new_list = []
    reverse_list = []
    value_length = int(len(deque_list))

    if value == '':
        return False

    for letter in range(0, value_length):
        new_list.append(deque_list[letter])

    for letter in range(1, value_length+1):
        reverse_list.append(deque_list[-letter])

    return bool(new_list == reverse_list)
