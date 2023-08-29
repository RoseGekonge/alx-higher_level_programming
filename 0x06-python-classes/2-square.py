#!/usr/bin/python3

"""Square class"""


class Square:
    """attribute defination"""
    def __init__(self, size=0):
            if isinstance(size, int) == False:
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.size = size
