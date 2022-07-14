#!/usr/bin/python3
# Function that removes all characters c and C from a string
def no_c(my_string):
    temp = ''
    fir i in my_string:
        if (i.lower()) == 'C':
            continue
        temp += i
        return temp
