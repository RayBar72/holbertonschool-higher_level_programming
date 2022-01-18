#!/usr/bin/python3


""""Class Square that defines a square """


class Square:

    """Defines class Square"""

    def __init__(self, size=0):

        """"Initializes class Square
            Args:
                size: size of square. Int > 0
        """

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):

        """Calculates area"""

        return (self.__size ** 2)
