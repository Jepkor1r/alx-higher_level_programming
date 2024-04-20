#!/usr/bin/python3

def remove_char_at(str, n):
    """
    remove_char_at - removes the character on position n
    str - the string to be checked
    n - the position of the character in string to be removed
    """
    if len(str) < n >= 0:
        print("{} + {}".format(str[:n], str[n+1:]))
