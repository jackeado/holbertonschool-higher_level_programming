#!/usr/bin/python3
"""
Contains a Base class
"""
import json


class Base:
    """A Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @classmethod
    def to_json_string(cls, list_dictionaries):
        """JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        dic = []
        if list_objs is not None:
            for i in list_objs:
                dic.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding="utf8") as n_file:
            n_file.write(cls.to_json_string(dic))

    @classmethod
    def from_json_string(cls, json_string):
        """list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            lista_ = []
            return lista_
        else:
            lista_ = json.loads(json_string)
            return lista_

    def create(cls, **dictionary):
        """Returns an Instance with all attributes already set:"""
        if cls.__name__ is "Rectangle":
            dummy = cls(3, 5)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ is "Square":
            dummy = cls(5)
            dummy.update(**dictionary)
            return dummy
