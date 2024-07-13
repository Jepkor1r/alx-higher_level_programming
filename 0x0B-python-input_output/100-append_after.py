#!/usr/bin/python3
"""
    A module that manipulates a text file by search andd write
"""


def append_after(filename="", search_string="", new_string=""):
    """
        A function that takes a file , search for a string and write
    """
    with open(filename, "r+", encoding="utf-8") as f:
        data = f.read()
