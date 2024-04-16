#!/usr/bin/python3

def islower(c):
    """islower() - function that checks lowercase
       c - is the parameter passed
       Return True if lowercase otherwise false
    """
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
