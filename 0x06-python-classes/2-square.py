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
    def __init__(self, __size):
        """
            init: used to initialize a instance
            self: self initializing instance attribute
            __size: private instance attribute
        """
        self.__size = __size

    try:
        def __init__(self, size=0):
            """
                init: used to initialize an instance
                self: self initializing instance attribute
                size: instance attribute
            """
            self.size = size
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
