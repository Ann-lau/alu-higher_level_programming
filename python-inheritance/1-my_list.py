#!/usr/bin/python3
"""class MyList that inheerits from list"""


class MyList(list):
    """class MyList inherits from list"""

    def print_sorted(self):
        """prints sorted lists"""
        temp_list = self[:]
        temp_list.sort()
        print("{}".format(temp_list))
