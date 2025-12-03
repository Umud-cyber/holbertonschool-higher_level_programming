#!/usr/bin/python3
def pascal_triangle(n):
    """Return Pascal's triangle of n rows."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # hər sətrin başlanğıcı
        row = [1]

        # ortadakı elementlər
        if i > 0:
            prev = triangle[i - 1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)

        triangle.append(row)

    return triangle
