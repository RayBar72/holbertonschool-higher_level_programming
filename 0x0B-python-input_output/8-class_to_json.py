#!/usr/bin/python3
"""
Modulus that contain function that returns
the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Function that returns the dictionary
    description with simple data structure
    """
    return obj.__dict__
