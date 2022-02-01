#!/usr/bin/python3
"""
Modulus that contains a function that writes string appending
"""


def append_write(filename="", text=""):
    """
    Function that writes a string in a file appending
    Return number of printed chars
    """
    with open(filename, encoding='utf-8', mode='a') as file_a:
        i = 0
        i = file_a.write(text)
        return i
