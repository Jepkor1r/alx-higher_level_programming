#!/usr/bin/python3
"""
    This module adds two integers
    add_integer: is the function
    args: a, b = 98
    Return: a + b
"""

def add_integer(a, b=98):
    """
        Adds two integers or after casting float to integers
        Arguments:
            a: first number, must be an integer or float
            b: second number(default = 98), must be an integer or float
        Raises:
            TypeError: if either a or b is not an integer or float
        Return:
            sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer") 
    a = int(a)
    b = int(b)
    return a + b
