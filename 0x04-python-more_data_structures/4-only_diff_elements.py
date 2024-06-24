#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    different1 = set_1.difference(set_2)
    different2 = set_2.difference(set_1)
    new_set = different1.union(different2)
    return new_set
