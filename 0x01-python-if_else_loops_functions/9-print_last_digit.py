#!/usr/bin/python3

def print_last_digit(number):
    """
        print_last_digit - prints the last digit of number
        number - parameter value to be checked
	Return - value of last digit
    """
    for num in number:
        if num == number[-1]:
            print("{}".format(num), end="")
