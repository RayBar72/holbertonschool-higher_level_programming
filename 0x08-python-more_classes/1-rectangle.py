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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrive width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Property to se width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise TypeError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property to retrive height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Property to se height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise TypeError("height must be >= 0")
        self.__height = height
