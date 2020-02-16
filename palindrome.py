from collections import deque

def is_plaindrome(value: str):
    deque_list = deque(value)
    new_list = []
    reverse_list = []
    value_length = int(len(deque_list))

    for letter in range(0, value_length):
        new_list.append(deque_list[letter])

    for letter in range(1, value_length+1):
        reverse_list.append(deque_list[-letter])

    if new_list == reverse_list:
        print(True)
    else:
        print(False)
    return reverse_list
