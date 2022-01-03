#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    x, y, i, j = 0, 0, 0, 0
    if len(tuple_a) == 1:
        x = tuple_a[0]
    if len(tuple_b) == 1:
        i = tuple_b[0]
    if len(tuple_a) > 1:
        x = tuple_a[0]
        y = tuple_a[1]
    if len(tuple_b) > 1:
        i = tuple_b[0]
        j = tuple_b[1]
    tuple_c = (x + i, y + j)
    return tuple_c
