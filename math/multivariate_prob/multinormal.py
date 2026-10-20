#!/usr/bin/env python3
"""Defines a multivariate normal distribution."""

import numpy as np


class MultiNormal:
    """Represents a multivariate normal distribution."""

    def __init__(self, data):
        """Initializes the distribution using the given data."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (n - 1)
