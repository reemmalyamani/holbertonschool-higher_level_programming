#!/usr/bin/python3
"""Generate Pascal's Triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
