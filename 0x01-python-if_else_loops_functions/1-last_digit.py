#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * -1
    if num % 10 > 5:
        print("Last digit of {} is {}". format(number, -1*(num % 10)), end="")
        print(" and is greater than 5")
    elif num % 10 == 0:
        print("Last digit of {} is {} and is 0". format(number, -1*(num % 10)))
    else:
        print("Last digit of {} is {}". format(number, -1*(num % 10)), end="")
        print(" and is less than 6 and not 0")

else:
    if number % 10 > 5:
        print("Last digit of {} is {}". format(number, number % 10))
        print(" and is greater that 5")
    elif number % 10 == 0:
        print("Last digit of {} is {} and is 0". format(number, number % 10))
    else:
        print("Last digit of {} is {}". format(number, number % 10), end="")
        print(" and is less than 6 and not 0")
