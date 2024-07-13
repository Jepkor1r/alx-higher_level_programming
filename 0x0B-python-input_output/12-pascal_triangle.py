#!/usr/bin/python3
"""

    This module returns a list of lists of integers
    representing the Pascal’s triangle of n

"""


def pascal_triangle(n):
    """
        function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    temp = []
    list = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(list[j] + list[j - 1])
        list = row
        temp.append(row)
    return temp
