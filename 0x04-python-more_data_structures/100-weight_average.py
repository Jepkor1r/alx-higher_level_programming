#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for row in my_list:
        mul = row[0] * row[1]
        score += mul
        weight += row[1]
    # calculate average in an efficient snd clean way
    average = score / weight
    return average
