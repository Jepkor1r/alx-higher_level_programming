#!/usr/bin/python3

def magic_calculation(a, b):
    try:
        result = 0
        for i in range(1, 3):
            if a > i:
                result += i + (a * b)
            else:
                result += i / (a + b)
    except Exception as e:
        print("Too far")
    finally:
        result += a + b
    return result
