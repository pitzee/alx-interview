#!/usr/bin/python3
"""
that returns a list of lists of integers representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """
    Check if n is less than or equal to 0

    """
    if n <= 0:
        return []

    triangle = [[1]]  

    # Iterate from i = 1 to n - 1 to generate each subsequent row
    for i in range(1, n):
        row = [1]

        # Iterate from j = 1 to i - 1 to calculate the values of the elements between the first and last elements of the row
        for j in range(1, i):
            # Calculate the value of each element using the values from the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  
        triangle.append(row)

    return triangle
