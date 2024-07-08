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

    characters = [".", "?", ":"]
    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result = result.strip()
            result += "\n\n"
        i += 1
    print(result.strip())
