#!/usr/bin/python3
"""
Modulus that reads a text file and prints to stdout
"""


def read_file(filename=""):
    """
    Function that read text file and prints it
    """
    with open(filename, encoding='utf-8') as file_a:
        print("{:s}".format(file_a.read()), end="")
