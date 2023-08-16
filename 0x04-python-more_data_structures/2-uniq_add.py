#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)

    sum = 0
    for r in new_list:
        sum += r
    return sum
