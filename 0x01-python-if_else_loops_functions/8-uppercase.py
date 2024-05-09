#!/usr/bin/python3

def uppercase(str):
    """
       uppercase() - prints a string in uppercase
       str - parameter passed
    """
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            print("{}".format(chr(ord(i) - 32)), end="")
