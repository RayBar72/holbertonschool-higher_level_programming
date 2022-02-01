#!/usr/bin/python3
"""
Modulus that has a function returning python rep of an JSON
"""
import json


def from_json_string(my_obj):
    """
    Function that returns the python
    representation of an JSON (string)
    """
    x = json.loads(my_obj)
    return x
