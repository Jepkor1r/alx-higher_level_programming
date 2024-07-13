#!/usr/bin/python3
import json
"""

    This module returns the JSON representation of an object (string)

"""


def to_json_string(my_obj):
    """
        function that returns the JSON representation of an object (string)
        Arguments:
            my_obj: python object to be serialized
        Returns: json string
    """
    json_string = json.dumps(my_obj)
    return json_string
