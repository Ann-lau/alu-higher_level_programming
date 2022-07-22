#!/usr/bin/python3
"""
Defines class rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        """
        creating instances with args:
        width=0 and height=0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Sets and gets private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        sets and gets instance attribute height
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeErroe("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        rectangle_area = self.__width * self.__height
        return rectangle_area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        rectangle_perimeter = ((self.__width*2) + (self.__height*2))
        return rectangle_perimeter

    def __str__(self):
        """Returns the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for i in range(self.__height):
            [rectangle.append(str(self.print_symbol))
             for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
