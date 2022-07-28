#!/usr/bin/python3
"""Inherits BaseGeometry class"""


BaseGeometry = __import__('7-base-geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """initializes data"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns [Square] <width>/<heigtht>."""
        return super().__str__()
