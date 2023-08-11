#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for r in dir(hidden_4):
        if r[0:2] != "__":
            print("{:s}".format(r))
