#!/usr/bin/python3
"""  module contains algorithm that rotates a 2d array 90 degrees """


def rotate_2d_matrix(matrix):
    n = len(matrix)
    x = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n-1, -1, -1):
            x[i].append(matrix[j][i])

    matrix[:] = x

    for z in matrix:
        print(z)
