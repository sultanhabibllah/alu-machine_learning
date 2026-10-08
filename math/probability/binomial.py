#!/usr/bin/env python3
"""Module for the Binomial probability distribution."""


class Binomial:
    """Represent a binomial probability distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the binomial distribution."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")

            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data)
            variance /= len(data)

            self.p = 1 - (variance / mean)
            self.n = round(mean / self.p)
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Calculate the binomial probability mass function."""
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        coefficient = 1
        for i in range(1, k + 1):
            coefficient = coefficient * (self.n - i + 1) / i

        return (coefficient * self.p ** k *
                (1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """Calculate the binomial cumulative distribution function."""
        k = int(k)

        if k < 0:
            return 0

        probability = 0
        for i in range(min(k, self.n) + 1):
            probability += self.pmf(i)

        return probability
