#!/usr/bin/python3
"""

    This function multipliesctwo matrices

"""


def matrix_mul(m_a, m_b):
    """"
        matrix_mul: function that multiplies two matrices
        Args:
            m_a: matrix one
            m_b: matrix two
        Return: multiplication of m_a by m_b
        Raises:
            TypeError: if m_a or m_b is not a list
            TypeError: if m_a or m_b is not a list of lists
            ValueError: if m_a or m_b is empty
            TypeError: if one element of list of lists is not integer or float
            TypeError: if m_a and m_b is not of the same size
            ValueError: if m_a and m_b cant be multiplied
    """
    if not m_a or not all(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(row for row in m_b):
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same ")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    for row in m_a:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])
    if cols_a != rows_b:
        raise TypeError("m_a and m_b can't be multiplied")

    new_matrix = []
    for row in m_a:
        new_row = []
        for j in range(cols_b):
            sum = 0
            for k in range(cols_a):
                sum += row[k] * m_b[k][j]
            new_row.append(sum)
        new_matrix.append(new_row)
    
    return new_matrix
