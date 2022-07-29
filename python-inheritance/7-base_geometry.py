#!/usr/bin/python3
"""empty BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator if less than 0 or not int"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
