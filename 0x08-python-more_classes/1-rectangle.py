#!/usr/bin/python3
"""
    Function that defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self, width=0, height=0):
        """
            Definition of class Rectangle.
                Args:
                    width: of the rectangle
                    height: of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Property to retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property to se width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrive height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property to se height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
