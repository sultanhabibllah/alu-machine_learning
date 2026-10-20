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

    def pdf(self, x):
        """Calculates the PDF at a given data point."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        d = self.mean.shape[0]

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        diff = x - self.mean

        numerator = np.exp(
            -0.5 * np.matmul(
                np.matmul(diff.T, np.linalg.inv(self.cov)), diff
            )[0, 0]
        )

        denominator = ((2 * np.pi) ** (d / 2)) * np.sqrt(
            np.linalg.det(self.cov)
        )

        return numerator / denominator
