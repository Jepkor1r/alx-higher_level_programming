#!/usr/bin/python3
"""
    This module prints a square with the character #
    print_square; is the function
    Args: size
    Prints: a square with the character #
    Raises:
        TypeError: size must be integer
        ValueError: if size is less than 0
	Typerror: if size is a float and is less than 0
"""
def print_square(size):
    """
        It prints a square with the character #
        Args:
            size: size length of the square
        Prints: a square with the character #
        Raises:
            TypeError: size must be integer
            ValueError: if size is less than 0
            Typerror: if size is a float and is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
