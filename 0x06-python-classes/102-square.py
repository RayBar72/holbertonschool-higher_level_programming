#!/usr/bin/python3


""""Class Square that defines a square """


class Square:

    """Defines class Square"""

    def __init__(self, size=0):

        """"Initializes class Square
            Args:
                size: size of square. Int > 0
        """

        self.size = size

    @property
    def size(self):

        """Gets the size"""

        return self.__size

    @size.setter
    def size(self, value):

        """Sets size
            Args:
            n: value of Square
        """

        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):

        """Calculates area"""

        return (self.__size ** 2)

    def __eq__(self, other):
        """Return comp equal"""

        return self.size == other.size

    def __ne__(self, other):
        """Return comp equal"""

        return self.size != other.size

    def __gt__(self, other):
        """Return comp equal"""

        return self.size > other.size

    def __lt__(self, other):
        """Return comp equal"""

        return self.size < other.size

    def __ge__(self, other):
        """Return comp equal"""

        return self.size >= other.size

    def __le__(self, other):
        """Return comp equal"""

        return self.size <= other.size
