#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Fuction that returns a list of list of ints
    """
    pascal = [[]]
    if n <= 0:
        return pascal
    i = 0
    pascal = []
    for row in range(n):
        i += 1
        lista = []
        for x in range(i):
            lista.append(0)
        pascal.append(lista)
    j = 0
    i = 0
    largo = 0
    for row in pascal:
        largo += 1
        for i in range(largo):
            if i == 0 or i == (largo - 1):
                pascal[j][i] = 1
                i += 1
            elif largo > 2 and pascal[j][i] == 0:
                pascal[j][i] = pascal[j - 1][i - 1] + pascal[j - 1][i]
                i += 1
            i += 1
        i = 0
        j += 1
    return pascal
