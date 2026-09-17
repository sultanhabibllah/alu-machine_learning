#!/usr/bin/env python3
"""Module for concatenating NumPy arrays."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along an axis."""
    return np.concatenate((mat1, mat2), axis=axis)
