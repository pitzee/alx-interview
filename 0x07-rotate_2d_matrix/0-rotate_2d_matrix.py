#!/usr/bin/python3
"""  module contains algorithm that rotates a 2d array 90 degrees """


def rotate_2d_matrix(matrix):

    x = [[] for q in range(len(matrix))]

    n = (len(matrix) - 1)
    m = 0

    for i in matrix:
        for j in i:
            x[m].append(matrix[n][m])
            n -= 1
        n += len(matrix)
        m += 1

    for z in x:
        print(z)
