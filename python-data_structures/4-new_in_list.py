#!/usr/bin/python3
# Replaces an element in a list without modifying the original list
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return new_list
new_in_list(my_list, idx, element)
