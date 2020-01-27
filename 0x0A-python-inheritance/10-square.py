#!/usr/bin/python3
"""
class BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """Class Base"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
