#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            print("FizzBuzz", end=" ")
        elif (i + 1) % 3 == 0:
            print("Fizz", end=" ")
        elif (i + 1) % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i + 1), end=" ")
