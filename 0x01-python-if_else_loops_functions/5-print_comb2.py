#!/usr/bin/python3

for i in range(100):
    if(i <= 9):
        print("0{}, ".format(i), end='')
    else:
        print("{}, ".format(i) if i < 99 else "{}{}".format(i, "\n"), end='')
