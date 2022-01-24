#!/usr/bin/python3
"""
    Function that defines a rectangle
"""


class Rectangle:
    """
    Class Rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Definition of class Rectangle.
                Args:
                    width: of the rectangle
                    height: of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Function that returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """str method to retur a rectangle made with char '#'"""
        out = ""
        if self.__width == 0 or self.__height == 0:
            return out
        else:
            i = self.__height
            while i:
                out += "#" * self.__width
                if i != 1:
                    out += "\n"
                i += -1
            return out

    def __repr__(self):
        """repr method to retur a rectangle made with char '#'"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Printing menssage when deleting"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
