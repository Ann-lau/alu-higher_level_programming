#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Returns [Rectangle] <width>/<height>"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Area of the rectangle"""

        return self.__width * self.__height
