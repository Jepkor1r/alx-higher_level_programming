#!/usr/bin/python3

def uppercase(str):
    """
       uppercase() - prints a string in uppercase
       str - parameter passed
    """
    for i, letter in enumerate(str):
        x = ord(letter)
        print(
            "{}".format(chr(x - 32))
            if ord('a') <= x <= ord('z')
            else "{}".format(letter), end="\n"
            if i == len(str) - 1 else "")
