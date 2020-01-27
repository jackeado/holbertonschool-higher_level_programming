#!/usr/bin/python3
"""
Cotains class student
"""


class Student:
    """Representation of Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for i in attrs:
            try:
                n_dict[i] = self.__dict__[i]
            except:
                pass
        return n_dict

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
