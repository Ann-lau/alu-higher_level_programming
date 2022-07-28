#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator"""
        if value != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
