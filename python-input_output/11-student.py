#!/usr/bin/python3
"""
class Student that defines a student
based on 9-student.py
"""


class Student:
    """defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of a student"""

        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp

    def reload_from_json(self, json):
        """reload from json"""

        for items in json.keys():
            self.__dict__[items] = json[items]
