#!/usr/bin/python3

"""Square class"""


class Square:
    """attribute defination"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or (len(tuple) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return int(self.__size) ** 2

    def my_print(self):
        if self.size == 0:
            print(end="\n")
        else:
            for i in range(self.size):
                for g in range(self.__position[0]):
                    print(end=" ")
                for r in range(self.size):
                    print("#", end="")
                print(end="\n")
