#!/usr/bin/python3
def uniq_add(my_list=[]):
    nuevo = set(my_list)
    suma = 0
    for x in nuevo:
        suma += x
    return suma
