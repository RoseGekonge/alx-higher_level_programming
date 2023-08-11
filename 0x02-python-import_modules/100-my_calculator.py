#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    else:
        if argv[2] == '+':
            print("{}".format(add(argv[1], argv[3])))
        elif argv[2] == '-':
            print("{}".format(sub(argv[1], argv[3])))
        elif argv[2] == '*':
            print("{}".format(mul(argv[1], argv[3])))
        elif argv[2] == '/':
            print("{}".format(div(argv[1], argv[3])))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit 1

