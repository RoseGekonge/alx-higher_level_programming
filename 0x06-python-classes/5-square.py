#!/usr/bin/python3

"""Square class"""


class Square:
    """attribute defination"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if size == 0:
            print(end="\n")
        else:
            for i in range(size):
                for r in range(size):
                    print("#", end="")
                print(end="\n")
