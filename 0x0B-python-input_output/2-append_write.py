#!/usr/bin/python3
"""

    This module appends a string at the end of a text file (UTF8)
    and returns the number of characters added

"""


def append_write(filename="", text=""):
    """
        function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added
        Arguments:
            filename(str): name of file
            text(str): text to be written
        Returns: number of characters added
    """
    if filename is None:
        filename = "filename.txt"
    with open(filename, "a", encoding="UTF-8") as f:
        content = f.write(text)
    return content
