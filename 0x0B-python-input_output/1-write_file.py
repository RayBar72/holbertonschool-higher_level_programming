#!/usr/bin/python3
"""
Modulus that contains a function that writes string
"""


def write_file(filename="", text=""):
    """
    Function that writes a string in a file
    Return number of printed chars
    """
    with open(filename, encoding='utf-8', mode='w') as file_a:
        i = 0
        i = file_a.write(text)
        return i
