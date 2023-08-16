#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uncommon_list = []
    common_list = []
    for r in set_1:
        for k in set_2:
            if r == k:
                common_list.append(k)
            else:
                continue
    for g in set_1:
        if g in common_list:
            continue
        else:
            uncommon_list.append(g)
    for g in set_2:
        if g in common_list:
            continue
        else:
            uncommon_list.append(g)
    return sorted(uncommon_list)
