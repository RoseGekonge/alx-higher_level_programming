#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    g = 0
    for k in my_list:
        g += 1
    for r in range(x):
        try:
            if r == g:
                print("\n", end="")
                return(g)
            else:
                print(my_list[r], end="")
        except x is not int:
            exit(1)
    print("\n", end="")
    return(x)
