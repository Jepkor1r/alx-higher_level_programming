#!/usr/bin/python3

def remove_char_at(str, n):
    """
    remove_char_at - removes the character on position n
    str - the string to be checked
    n - the position of the character in string to be removed
    """
    if n > len(str):
        return str
    new_string = ""
    for i in str:
        matched_letter = str[n]
        if i != matched_letter:
            new_string += i
    return new_string
