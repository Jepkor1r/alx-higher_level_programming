#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        num = i[0]
        num += num
        print("{:d}".format(num))
