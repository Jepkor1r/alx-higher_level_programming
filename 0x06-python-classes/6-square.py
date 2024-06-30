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
    def __init__(self, size=0, position=(0, 0)):
        """
            init: used to initialize an instance
            self: self initializing instance attribute
            size: instance attribute
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
            size: method used for geting data is decorated with '@property'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            setter: for changing data
            @size: decorates setter with method name of the property decorator
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not (isinstance(value, tuple) and len(value) == 2 and position > 0):
            raise TypeError("position must be a tuple of 2 positive integers")
    
    def area(self):
        """
            area: used to calculate the area of squared size
            return : area of a squared size
        """
        return self.__size ** 2
        return area(self.__size ** 2)

    def my_print(self):
        """
            my_print: prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size) 
