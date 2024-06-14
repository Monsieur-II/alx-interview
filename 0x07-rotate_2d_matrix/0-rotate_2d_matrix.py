#!/usr/bin/python3
"""module Rotate 2D Matrix"""


def rotate_2d_matrix(matrix) -> None:
    """
    Method:
        Given an n x n 2D matrix,
        rotate it 90 degrees clockwise.
    Args:
        matrix List[List]: matrix.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
