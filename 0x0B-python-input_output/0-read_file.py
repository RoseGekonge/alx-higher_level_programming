#!/usr/bin/python3
"""reads external files"""


def read_file(filename=""):
    """function that reads into files"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
