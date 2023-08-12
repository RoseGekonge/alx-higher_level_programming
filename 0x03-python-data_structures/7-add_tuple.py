#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    i = 0
    while True:
        if i == len(tuple_a):
            new_tuple += tuple_b[i:len(tuple_b)]
            break
        elif i == len(tuple_b):
            new_tuple += tuple_a[i:len(tuple_a)]
            break
        else:
            new_tuple = new_tuple + (int(int(tuple_a[i]) + int(tuple_b[i])),)
            i += 1
    return new_tuple
