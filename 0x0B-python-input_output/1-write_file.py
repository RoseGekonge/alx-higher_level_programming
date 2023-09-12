#!/usr/bin/python3
"""writes into an external file"""


def write_file(filename="", text=""):
    """function that overwrites into a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written
