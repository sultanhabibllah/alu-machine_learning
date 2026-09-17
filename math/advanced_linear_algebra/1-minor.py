#!/usr/bin/env python3
"""Module for calculating the minor matrix."""


def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    if matrix == [[]]:
        return 1
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - \
            matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(len(matrix)):
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix."""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if len(matrix) == 1:
        return [[1]]

    minors = []
    for i in range(len(matrix)):
        row_minors = []
        for j in range(len(matrix)):
            submatrix = [
                row[:j] + row[j + 1:]
                for row in matrix[:i] + matrix[i + 1:]
            ]
            row_minors.append(determinant(submatrix))
        minors.append(row_minors)
    return minors
