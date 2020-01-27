#!/usr/bin/python3
"""
Contains a class Student
"""


class Student:
    """Representation of Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for i in attrs:
            try:
                n_dict[i] = self.__dict__[i]
            except:
                pass
        return n_dict
