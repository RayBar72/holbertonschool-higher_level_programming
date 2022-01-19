#!/usr/bin/python3


""""Class Square that defines a square """


class Square:

    """Defines class Square"""

    def __init__(self, size=0, position=(0, 0)):

        """"Initializes class Square
            Args:
                size: size of square. Int > 0
                position: size of square. Int > 0
        """

        self.size = size
        self.position = position

    @property
    def size(self):

        """Gets the size"""

        return self.__size

    @property
    def position(self):

        """Gets the position"""

        return self.__position

    @size.setter
    def size(self, value):

        """Sets size
            Args:
                value: value of Square
        """

        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):

        """Sets size
            Args:
                value: value of Square
        """

        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        """Calculates area"""

        return (self.__size ** 2)

    def my_print(self):

        """Prints in stdout # to form a square"""

        if self.__size == 0:
            print()
        else:
            i = 0
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            while i < self.__size:
                i += 1
                if self.__position[0] > 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
