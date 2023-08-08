#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b < 0:
        c = b * -1
    else:
        c = b
    for i in range(0, c):
        result = result * a
    if b < 0:
        result = 1/result
    else:
        result = result
    return result
