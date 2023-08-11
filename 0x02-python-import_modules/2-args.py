#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    if len_argv < 2:
        print("0 arguments.")
    elif len_argv == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len_argv - 1))
    for i in range(1, len_argv):
        print("{}: {}".format(i, sys.argv[i]))
