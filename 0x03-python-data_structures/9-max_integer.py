#!/usr/bin/python3

def max_integer(my_list=[]):
	if my_list != None:
	    new_list = my_list.sort()
	    new_list1 = new_list.reverse()
	    max_value = newlist1[0]
	    return max_value
	else:
	    return None
