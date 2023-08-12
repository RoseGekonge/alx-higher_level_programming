#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    i = 0
    while i != 2:
        if i >= len(tuple_a) and i >= len(tuple_b):
            new_tuple = new_tuple + (0,)
        elif i >= len(tuple_a):
            new_tuple = new_tuple + (int(0 + int(tuple_b[i])),)
        elif i >= len(tuple_b):
            new_tuple = new_tuple + (int(int(tuple_a[i]) + 0),)
        else:
            new_tuple = new_tuple + (int(int(tuple_a[i]) + int(tuple_b[i])),)
        i += 1
    return new_tuple
