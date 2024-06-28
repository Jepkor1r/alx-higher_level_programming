#!/usr/bin/python3

def uppercase(str):
    """
       uppercase() - prints a string in uppercase
       str - parameter passed
    """
    result = ""
    for i in str:
        x = ord(i)
        if ord('a') <= x <= ord('z'):
            letter = chr(x - 32)
            result += letter
        else:
            result += i
        result += "\n" if not str else ""
    print("{}".format(result))
