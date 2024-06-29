#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
	for i in range(list_length):
          
        result = my_list_1[0] / my_list_2[1]
    except (ValueError, TypeError, IndexError):
        result = 0
    finally:
