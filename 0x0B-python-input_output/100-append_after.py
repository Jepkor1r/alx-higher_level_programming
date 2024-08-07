#!/usr/bin/python3
"""
    A module that manipulates a text file by search andd write
"""


def append_after(filename="", search_string="", new_string=""):
    """
        A function that takes a file , search for a string and write
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
