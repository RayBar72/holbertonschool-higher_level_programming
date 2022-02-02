#!/usr/bin/python3
"""
Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    i = 0
    with open(filename, mode='r+', encoding='utf-8') as file_a:
        lectura = file_a.readlines()
    with open(filename, mode='w', encoding='utf-8') as file_b:
        for lines in lectura:
            i += 1
            if search_string in lines:
                lectura.insert(i, new_string)
        for lines in lectura:
            file_b.write(lines)
