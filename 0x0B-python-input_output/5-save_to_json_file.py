#!/usr/bin/python3
"""

    This module writes an Object to a text file, using a JSON representation

"""
import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file, using a JSON repr.
        Arguments:
            my_obj: object to be decoded
            filename: name of the file
    """
    my_string = json.dumps(my_obj)
    with open(filename, "w", encoding="UTF-8") as f:
        content = f.write(my_string)
    return content
