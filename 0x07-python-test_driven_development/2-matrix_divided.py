#!/usr/bin/python3
""""
    Modulus that divides a matrix
    matrix: matrix to be divided
    div: divisor
"""


def matrix_divided(matrix, div):
    """
        Function that divides a matrix
    """
    marro = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not any(matrix):
        raise TypeError(marro)
    if type(matrix) != list:
        raise TypeError(marro)
    for row in matrix:
        if type(row) != list:
            raise TypeError(marro)
        for value in row:
            if type(value) != int and type(value) != float:
                raise TypeError(marro)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(value / div, 2) for value in row] for row in matrix]
