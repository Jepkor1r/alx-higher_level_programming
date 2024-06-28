#!/usr/bin/python3

def print_last_digit(number):
    """
        print_last_digit - prints the last digit of number
        number - parameter value to be checked
        Return - value of last digit
    """
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
