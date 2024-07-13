#!/usr/bin/python3
"""

    In this module, class Student defines a student

"""


class Student:
    """
        class Student that defines a student by:
        Public instance attributes:
            first_name
            last_name
            age
        Instantiation with first_name, last_name and age
        Public method(to_json) retrieves dictionary repr. of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes the student instance with first_name,last_name,age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            public method that retrieves a dict. repr. of Student instance

        """
        return self.__dict__
