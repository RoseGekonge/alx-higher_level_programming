#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for r in range(len(matrix[0])):
            if r == len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][r]), end="")
            else:
                print("{:d}".format(matrix[i][r]), end=" ")
        print("\n", end="")
