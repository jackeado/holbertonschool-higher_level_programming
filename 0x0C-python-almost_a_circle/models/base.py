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
    def to_json_string(cls, list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            json_s = json.dumps(list_dictionaries)
            return json_s

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        lista_d = []
        if list_objs is not None:
            for inst in list_objs:
                lista_d.append(inst.to_dictionary())
        with open(filename, encoding='utf-8', mode='w') as f:
            print(cls.to_json_string(lista_d))

    @classmethod
    def from_json_string(cls, json_string):
        if json_string is None or json_string == 0:
            lista_ = []
            return lista_
        else:
            lista_ = json.loads(json_string)
            return lista_
