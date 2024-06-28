#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list to store keys that need to be deleted
    delete_keys = [key for key in a_dictionary if a_dictionary[key] == value]
    # Delete the keys from the dictionary
    for key in delete_keys:
        del a_dictionary[key]
    return a_dictionary
