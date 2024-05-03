#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
       print("{}".format("\n") if my_list is None else "{:d}".format(i))
