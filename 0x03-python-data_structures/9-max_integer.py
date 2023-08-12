#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    for i in range(1, len(my_list)):
        if len(my_list) == 0:
            return None
        elif my_list[i] > largest:
            largest = int(my_list[i])
        else:
            continue
    return largest
