#!/usr/bin/python3
"""
Class Square: empty class
init: stands for initialization method
self: instance attribute
__size: private instance attribute
"""


class Square:
    """
        Square: an empty class
        It defines a class
    """
    def __init__(self, size=0):
        """
            init: used to initialize an instance
            self: self initializing instance attribute
            size: instance attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            self.__size = size
