#!/usr/bin/python3
"""
add_integer:
    Adds two ints if they are ints
    Return the sum of them
"""


def add_integer(a, b=98):
    """
    Adds two integers
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
