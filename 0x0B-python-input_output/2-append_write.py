#!/usr/bin/python3
"""appends into an external file"""


def append_write(filename="", text=""):
    """function that appends into a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written
