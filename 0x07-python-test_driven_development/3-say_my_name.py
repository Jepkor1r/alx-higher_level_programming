#!/usr/bin/python3
"""
    This module prints name
    say_my_name: is the function
    Args: first_name, last_name=""
    Prints: My name is <first name> <last name>
    Raises: TypeError, if first_name and last_name are not strings
"""


def say_my_name(first_name, last_name=""):
    """
        It prints name
        Args:
            first_name: must be string
            last_name: must be string , with default(last_name="")
        Prints: My name is <first name> <last name>
        Raises:
            TypeError: if first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
