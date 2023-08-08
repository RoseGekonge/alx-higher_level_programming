#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if x > i:
            if i == 8:
                print("{}".format((i*10) + x))
            else:
                print("{:02}".format((i*10) + x), end=", ")
        else:
            continue
