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

    def to_json(self, attrs=None):
        """
            public method that retrieves a dict. repr. of Student instance
            If attrs is a list of strings,
            only attribute names contained in this list are retrieved
        """
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[elements], str) for elements in attrs):
            return self.__dict__
        return {key: value for key, value in self.__dict__.items()
                if key in attrs}
