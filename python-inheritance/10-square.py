#!/usr/bin/python3
"""Inherits BaseGeometry class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""

    def __init__(self, size):
        """initializes data"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size