#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    while i != 0:
        i -= 1
        print("{}".format(int(my_list[i])))