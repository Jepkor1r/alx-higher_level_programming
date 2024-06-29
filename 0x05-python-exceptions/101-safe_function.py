#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        # fct: function name to be called
        # *args: any number of arguments is accepted
        # for example: add(1, 2, 3)
        # add is the function while (1, 2, 3) are arguments
        # So *args is like?
        # having a box to hold any number of balls yet you dont know how many
        return fct(*args)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
