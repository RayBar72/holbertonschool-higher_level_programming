#!/usr/bin/python3
"""
Modulus that write a function that creates an Object from a JSON
"""
import json


def load_from_json_file(filename):
    """
    Function that write a function that creates an Object
    from a JSON
    """
    with open(filename, mode='r', encoding='utf-8') as file_a:
        return json.load(file_a)
