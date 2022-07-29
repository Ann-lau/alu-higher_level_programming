#!/usr/bin/python3
"""class Mylist that inherits from list"""


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints sorted list"""
        temp_list = self[:]
        temp_list.sort()
        print("{}".format(temp_list))
