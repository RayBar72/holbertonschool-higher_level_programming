#!/usr/bin/python3
"""
Modulus thah inherits int
"""


class MyInt(int):
    """
    Class that inherits from int
    """
    def __eq__(self, value):
        """
        Method equals
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """
        Method not equal
        """
        return super().__eq__(value)
