#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:\n1: {}".format(sys.argv[1]))
else:
    print("{} arguments:\n{}".format(len(sys.argv) - 1, "\n".join(["{}: {}".format(i, sys.argv[i]) for i in range(1, len(sys.argv))])))
