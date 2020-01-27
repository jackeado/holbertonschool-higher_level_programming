#!/usr/bin/python3
"""
Contains a Base class
"""
import json


class Base:
    """A Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
       if id is None:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
       else:
           self.id = id
    @classmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            json_s = json.dumps(list_dictionaries)
            return json_s

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        dic = []
        if list_objs is not None:
            for inst in list_objs:
                dic.append(cls.to_dictionary(dic))
        with open(filename, encoding='utf-8', mode='w') as json_file:
            json_file.write(cls.to_json_string(dic))

    # def save_to_file(cls, list_objs):
    #     """writes the JSON string representation of list_objs to a file"""
    #     filename = "{}.json".format(cls.__name__)
    #     dic = []
    #     if list_objs is not None:
    #         for i in list_objs:
    #             dic.append(cls.to_dictionary(i))
    #     with open(filename, 'w', encoding="utf8") as n_file:
    #         n_file.write(cls.to_json_string(dic))

