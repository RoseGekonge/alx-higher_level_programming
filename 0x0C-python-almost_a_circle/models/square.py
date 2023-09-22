#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class with defined attributes and methods"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, width, height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        my_dict = {}
        my_dict['id'] = self.__id
        my_dict['size'] = self.__size
        my_dict['x'] = self.__x
        my_dict['y'] = self.__y
        return my_dict
