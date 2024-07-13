#!/usr/bin/python3
"""

    This module reads a text file and prints it to stdout

"""


def read_file(filename=""):
    """
        Function that reads a text file and prints it to stdout
        Arguments:
            filename, UTF encoded
        with: used to close a file even if an exception is raised at some point
        Prints: the filename
    """
    with open(filename, encoding="UTF-8") as f:
        content = f.read()
    print(content, end='')
