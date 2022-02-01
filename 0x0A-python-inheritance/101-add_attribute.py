#!/usr/bin/python3
"""
Function that adds a new attribute
"""


def add_attribute(a, name, value):
    """
    Adds an attribute
    """
    not_add = {int, str, float, list, dict, tuple, frozenset, type, object}
    if type(a) in not_add:
        raise TypeError("can't add new attribute")
    a.__setattr__(name, value)
