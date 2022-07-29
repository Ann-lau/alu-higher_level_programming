#!/usr/bin/python3
"""class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """initializes square"""

        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size**2

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))


    if __name__ == '__main__':
        s = Square(13)

        print(s)
        print(s.area())
