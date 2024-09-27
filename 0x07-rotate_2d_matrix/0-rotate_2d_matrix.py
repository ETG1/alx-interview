#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square matrix (n x n) 90 degrees clockwise.
    The rotation is done in-place.

    Args:
    matrix (list of list of ints): The n x n 2D matrix to rotate.

    Returns:
    None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
