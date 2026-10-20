
#!/usr/bin/env python3
"""Calculates a correlation matrix from a covariance matrix."""

import numpy as np


def correlation(C):
    """Calculates the correlation matrix of C."""
    if not isinstance(C, np.ndarray) or C.ndim != 2:
        raise TypeError("C must be a 2D numpy.ndarray")

    if C.shape[0] != C.shape[1]:
        raise ValueError("C must be a square matrix")

    std = np.sqrt(np.diag(C))
    corr = C / np.outer(std, std)

    return corr

