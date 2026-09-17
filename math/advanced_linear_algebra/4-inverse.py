#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""
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


def inverse(matrix):
    """Calculate the inverse of a matrix."""
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    det = determinant(matrix)
    if det == 0:
        return None

    if len(matrix) == 1:
        return [[1 / det]]

    cofactors = []
    for i in range(len(matrix)):
        row_cofactors = []
        for j in range(len(matrix)):
            submatrix = [
                row[:j] + row[j + 1:]
                for row in matrix[:i] + matrix[i + 1:]
            ]
            value = determinant(submatrix) * ((-1) ** (i + j))
            row_cofactors.append(value)
        cofactors.append(row_cofactors)

    adjugate = [[cofactors[j][i] for j in range(len(matrix))]
                for i in range(len(matrix))]
    return [[value / det for value in row] for row in adjugate]
