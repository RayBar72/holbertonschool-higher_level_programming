#!/usr/bin/python3
"""
Class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inheritage from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation vars width and heigh
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
