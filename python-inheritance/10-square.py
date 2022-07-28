#!/usr/bin/python3
"""Inherits BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectabgle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """Initializes data"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns [square] <width>/<height>."""
        return super().__str__()

    def area(self):
        """Area oof Square"""

        return self.__size ** 2
