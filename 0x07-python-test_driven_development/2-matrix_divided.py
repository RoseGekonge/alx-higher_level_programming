#!/usr/bin/python3
'''divide the whole matrix by div:
    Args:
        matrix
        div
    Every element of the matrix is divided by div and saved in a new matrix called div_matrix.
    Returns:
        div_matrix'''

def matrix_divided(matrix, div):
    '''checks for TypeError and ZerDivisionError'''
    k = 0
    div_matrix = []
    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if isinstance(matrix, list) and not all(isinstance(item, list) for item in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        for i in range(len(matrix)):
            row = []
            if i != 0:
                if len(matrix[i]) != k:
                    raise TypeError("Each row of the matrix must have the same size")
            k = 0
            for r in range(len(matrix[0])):
                row.append(round(matrix[i][r] / div, 2))
                k += 1
            div_matrix.append(row)
    return div_matrix
