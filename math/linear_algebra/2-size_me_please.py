#!/usr/bin/env python3
"""Calculate the shape of a matrix."""


def matrix_shape(matrix):
    """Return the shape of a matrix as a list."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
