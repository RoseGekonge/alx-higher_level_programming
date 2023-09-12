#!/usr/bin/python3
"""reads external files"""


def read_file(filename=""):
    """function that reads into files"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
