#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = max(a_dictionary.values(), default=None)
    if max_value is None:
        return None
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
    return None
