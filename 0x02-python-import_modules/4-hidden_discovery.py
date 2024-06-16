#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    # dir function - list all attributes in hidden_4 module alphabetically
    for i in dir(hidden_4):
        # skips all attributes starting with "__"
        if i[:2] == "__":
            continue
        print("{:s}".format(i))
