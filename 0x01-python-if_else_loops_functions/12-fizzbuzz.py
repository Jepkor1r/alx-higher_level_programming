#!/usr/bin/python3

def fizzbuzz():
    """
    fizzbuzz - function that prints 1-100 separated by space
    Fizz - prints it instead of number for multiples of 3
    Buzz - prints it instead of number for multiples of 5
    FizzBuzz - prints it instead of number for multiples of both 3 and 5
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end='')
        elif i % 3 == 0:
            print("Fizz ", end='')
        elif i % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(i), end='')
