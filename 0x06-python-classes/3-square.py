#!/usr/bin/python3

"""Square class"""


class Square:
    """attribute defination"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return int(self.__size) ** 2
