#!/usr/bin/python3
"""
Modulus that has an script that adds all arguments to a
Python list, and then save them to a file
"""
import json
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_a = 'add_item.json'
file_exist = os.path.isfile(file_a)

if file_exist:
    lista = load_from_json_file(file_a)
else:
    lista = []

for arg in sys.argv:
    if arg == "./7-add_item.py":
        continue
    lista.append(arg)

save_to_json_file(lista, file_a)
