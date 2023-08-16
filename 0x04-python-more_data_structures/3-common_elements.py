#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_list = []
    for r in set_1:
        for k in set_2:
            if r == k:
                common_list.append(k)
            else:
                continue
    return common_list
