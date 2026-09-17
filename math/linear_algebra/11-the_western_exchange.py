#!/usr/bin/env python3
"""Module for transposing a NumPy array."""


def np_transpose(matrix):
    """Return the transpose of a NumPy array."""
    return matrix.transpose().copy()
