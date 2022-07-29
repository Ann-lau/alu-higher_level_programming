#!/usr/bin/python3
""" class Square that inherits from Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-base_geometry').Rectangle


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self size):
        """initializes data"""

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """returns [Square] <width>/<height>."""
        return str("[Square] {}/{}".fomat(self.__size, self.__size))

    def area(self):
        """area of Square"""

        return self.__size ** 2
