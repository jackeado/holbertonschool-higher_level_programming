#!/usr/bin/python3
"""
class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """"initalization the square"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
