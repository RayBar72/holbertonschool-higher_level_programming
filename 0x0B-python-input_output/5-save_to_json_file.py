#!/usr/bin/python3
"""
Modulus that write a function that writes an Object
to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object
    to a text file, using a JSON representation
    """
    with open(filename, mode='w', encoding='utf-8') as file_a:
        json.dump(my_obj, file_a)
