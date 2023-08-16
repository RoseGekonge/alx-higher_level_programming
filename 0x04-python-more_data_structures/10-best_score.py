#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    if a_dictionary is None:
        return None
    for i in a_dictionary:
        if a == 0:
            largest = i
        else:
            if a_dictionary.get(i) > a_dictionary.get(largest):
                largest = i
            else:
                continue
        a += 1
    return largest
