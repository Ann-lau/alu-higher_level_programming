#!/usr/bin/python3
"""class Mylist that inherits from list"""


class MyList(list):
    """MyList inherits from list"""
    def print_sorted(self):
        print(sorted(self))
