#!/usr/bin/python3
"""Pascal Triangle Interview Challenge, A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal_triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return pascal_triangle
    for i in range(n):
        sanna_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                sanna_list.append(1)
            else:
                sanna_list.append(pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j])
        pascal_triangle.append(sanna_list)
    # print(triangle)
    return pascal_triangle
