#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """Class Base"""
    def area(self):
        """raises an Exception Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if an int or grater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
