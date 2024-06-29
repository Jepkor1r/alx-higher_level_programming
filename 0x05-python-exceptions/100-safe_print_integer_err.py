#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    except (ValueError, TypeError) as e:
        # sys.stderr: redirects the error msg to standard error output stream
        # file was used to explicitly print stderr. Why?
        # by default print has  file parameter where output is to  be directed
        print(f"Exception: {e}", file=sys.stderr)
        return False
