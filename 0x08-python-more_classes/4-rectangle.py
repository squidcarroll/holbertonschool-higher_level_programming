#!/usr/bin/python3
"""
this class defines a rectangle
"""


class Rectangle:
    """This class defiens a rectangle

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        new_string = ""

        if self.width == 0 or self.height == 0:
            return new_string

        for x in range(self.height - 1):
            new_string += '#' * self.width + '\n'
        new_string += '#' * self.width

        return new_string

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
