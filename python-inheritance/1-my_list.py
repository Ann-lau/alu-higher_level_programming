#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """class MyList inherits list"""

    def pritn_sorted(self):
        """prints sorted list"""
        temp_list = self[:]
        temp_list.sort()
        print{("{}".format(temp_list))
