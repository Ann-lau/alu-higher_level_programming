#!/usr/bin/python3
# Prints all integers of a list in reverse order
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    else:
        for i in my_list[::-1]:
            print("{:d}".format(i))
