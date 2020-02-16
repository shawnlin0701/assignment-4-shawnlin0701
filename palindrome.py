from collections import deque

def is_palindrome(value: str):
    deque_list = deque(value)
    new_list = []
    reverse_list = []
    value_length = int(len(deque_list))
    if value == '':
        return False

    for letter in range(0, value_length):
        new_list.append(deque_list[letter])

    for letter in range(1, value_length+1):
        reverse_list.append(deque_list[-letter])

    if new_list == reverse_list:
        return True
    else:
        return False
    return reverse_list
