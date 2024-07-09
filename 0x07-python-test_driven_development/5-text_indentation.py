#!/usr/bin/python3
"""
    This module prints a text with 2 new lines,
    after each of these characters: ., ? and :
    text_indentation: this is the function
    Args: text, must be a string
    Print: a text with 2 new lines
    after each of these characters: ., ? and :
    Also, no space at the beginning or at the end of each printed line
    Raises: TypeError, if text is not a string
"""


def text_indentation(text):
    """
        It prints a text with 2 new lines,
        after each of these characters: ., ? and :
        with no space at the beginning or at the end
        Args:
            text, must be a string
        Print: text
        Raises:
         TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = " "
    erase_spaces = True

    for char in text:
        if char in ".?:":
            result += char + "\n\n"
            erase_spaces = True
        else:
            if char != " " or not erase_spaces:
                result += char
            erase_spaces = False

    if result.endswith("/n/n"):
        result = result[:-1]
    print(result.lstrip())
