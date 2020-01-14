#!/usr/bin/python3
"""


"""
def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    sizerow = None
    for lista in matrix:
        if type(lista) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if sizerow is None:
            sizerow = len(lista)
        elif sizerow != len(lista):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for i in lista:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")
    if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in lista] for lista in matrix]
