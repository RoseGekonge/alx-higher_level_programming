#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for g in range(1, 3):
        try:
            if (g > a):
                raise Exception('Too far')
            else:
                r += (a**b)/g
        except Exception:
            r = (b + a)
            break
    return r
