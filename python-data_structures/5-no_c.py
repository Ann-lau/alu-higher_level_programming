#!/usr/bin/python3
# Function that removes all characters c and C from a string
def no_c(my_string):
    my_string = list(filter((c, C).__ne__, my_string))
    print(my_string)
no_c(my_string)
