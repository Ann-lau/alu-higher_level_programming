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
            raise TypeError("{} must be an ineteger".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
