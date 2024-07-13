#!/usr/bin/python3
"""

    This module returns an object (Python data structure)
    represented by a JSON string using json.loads() method
"""
import json


def from_json_string(my_str):
    """
        function that returns an object (Python data structure)
        represented by a JSON string
        Arguments:
            my_str: json string to be decoded
        Return: python object
    """
    my_object = json.loads(my_str)
    return my_object
