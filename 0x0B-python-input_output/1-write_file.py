#!/usr/bin/python3
"""

    This module writes a string to a text file (UTF8)
    and returns the number of characters written

"""

def write_file(filename="", text=""):
    """
        This function writes a string to a text file (UTF8)
        and returns the number of characters written
        Arguments:
            filename(str): name of file
            text(str): text to write to file
        Returns: the number of characters of string
    """
    if filename is None:
        filename = "filename.txt"
    with open(filename, "w", encoding="UTF-8") as f:
        content = f.write(text)
    return content
