#!/usr/bin/env python3
"""Module for the Poisson probability distribution."""


class Poisson:
    """Represent a Poisson probability distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Poisson distribution."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculate the Poisson probability mass function."""
        k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        factorial = 1

        for i in range(1, k + 1):
            factorial *= i

        return (e ** (-self.lambtha) *
                self.lambtha ** k / factorial)

    def cdf(self, k):
        """Calculate the Poisson cumulative distribution function."""
        k = int(k)

        if k < 0:
            return 0

        probability = 0

        for i in range(k + 1):
            probability += self.pmf(i)

        return probability
