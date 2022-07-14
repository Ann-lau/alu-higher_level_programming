#!/usr/bin/python3
# Function that removes all characters c and C from a string
def no_c(my_string):
    temp = ''
    for i in my_string:
        if (i.lower()) == 'c':
            continue
        temp += i
        return temp
