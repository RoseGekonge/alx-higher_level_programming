#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        if number >= 0:
            print("{}".format(number % 10), end="")
        else:
            number = number * -1
    else:
        exit(1)
    return number % 10
