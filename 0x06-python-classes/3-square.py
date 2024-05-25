#!/usr/bin/python3
"""
Class Square: empty class
init: stands for initialization method
self: instance attribute
__size: private instance attribute
"""


class Square():
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
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
            area: used to calculate the area of squared size
            return : area of a squared size
        """
        return self.__size ** 2
        return area(self.__size ** 2)
