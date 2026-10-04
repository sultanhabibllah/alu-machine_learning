#!/usr/bin/env python3
"""Module for calculating the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculate the derivative of a polynomial."""
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [i * poly[i] for i in range(1, len(poly))]

    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()

    return derivative
