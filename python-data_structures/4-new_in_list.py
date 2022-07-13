#!/usr/bin/python3
# Replaces an element in a list without modifying the original list


def new_in_list(my_list, idx, element):
    if idx < 0:
        c = my_list[:]
        return c
    elif idx >= len(my_list):
        d = my_list[:]
        return d
    else:
        v = my_list[:]
        my_list[idx] = element
        return v
new_in_list(my_list, idx, element)
