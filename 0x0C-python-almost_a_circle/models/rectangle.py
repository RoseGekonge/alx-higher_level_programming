#!/usr/bin/python3
"""rectangle class"""
from models.base import Base
import tkinter as TK


class Rectangle(Base):
    """class with defined attributes and methods"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not value.isdigit():
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not value.isdigit():
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not value.isdigit():
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not value.isdigit():
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__width):
            for r in range(self.__x):
                print(end=" ")
            for k in range(self.__height):
                print(end="#")
            print(end="\n")
    def __str__(self):
        return "[" + str(self.__Rectangle) + "] (<" + str(self.__id) + ">) <" + str(self.__x) + ">/<" + str(self.__y) + "> - <" + str(self.__width) + ">/<" + str(self.__height) + ">"

    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def to_dictionary(self):
        my_dict = {}
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        my_dict['id'] = self.__id
        my_dict['height'] = self.__height
        my_dict['width'] = self.__width
        return my_dict
