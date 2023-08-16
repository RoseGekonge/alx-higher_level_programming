#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for r in range(len(matrix)):
        row = []
        for g in range(len(matrix[0])):
            row.append(matrix[r][g] * matrix[r][g])
        square_matrix.append(row)
    return square_matrix
