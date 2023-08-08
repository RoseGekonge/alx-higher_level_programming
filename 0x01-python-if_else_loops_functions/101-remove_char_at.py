#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""
    a = 0
    for i in range(len(str)):
        if i == n:
            continue
        else:
            new_string += str[i]
            a += 1
    return new_string
