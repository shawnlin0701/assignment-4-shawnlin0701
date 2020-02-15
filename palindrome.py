from collections import deque

def is_plaindrome(value: str):
    deque_list = deque(value)
    print(deque_list)
    value_length = int(len(deque_list))
    print(value_length)
    count = 0
    for letter in range(0, value_length//2):
        while deque_list[letter] == deque_list[value_length-1]:
            value_length -= 1
            count += 1
            print('count:', count)
            print('letter:', letter)
            print('length', value_length)

        if count == int(len(deque_list)//2):
            print(True)
    else:
        print(False)

is_plaindrome('123321')
