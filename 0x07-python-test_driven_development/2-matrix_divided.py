#!/usr/bin/python3
"""
    This module divides all elements of a matrix
    matrix_divided: is the function
    Args: matrix, div
    Returns: new_matrix with all elements divided by div,
    roundedto 2 dp
    Raises:
        TypeError
        ZeroDivisionError
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix.
        Args:
            matrix: must be a list of lists of integers/floats
            div: divisor, must be integer/float
        Returns:
            new matrix with all elements divided by div,
            rounded to 2 decimal places
        Raises:
            TypeError: if matrix is not a list of lists of integers/floats
                       if rows of matrix are not of the same size
                       if div is not a number
            ZeroDivisionError: if div is zero
    """
    listOfList = isinstance(matrix, list)
    messageError = "matrix must be a matrix (list of lists) of integers/floats"
    if not listOfList or not all(isinstance(row, list) for row in matrix):
        raise TypeError(messageError)
    row_length = len(matrix[0])
    for row in matrix:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError(messageError)
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i / div, 2))
        new_matrix.append(new_row)
    return new_matrix
