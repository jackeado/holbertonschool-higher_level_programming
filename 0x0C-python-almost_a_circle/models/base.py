#!/usr/bin/python3
"""
Contains a Base class
"""
import json
import csv
import turtle

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
        """writes the JSON string representation"""
        filename = "{}.json".format(cls.__name__)
        lista_d = []
        if list_objs is not None:
            for inst in list_objs:
                lista_d.append(inst.to_dictionary())
        with open(filename, encoding='utf-8', mode='w') as f:
            return f.write(cls.to_json_string(lista_d))

    @classmethod
    def from_json_string(cls, json_string):
        """list of the JSON string"""
        if json_string is None or len(json_string) == 0:
            lista_ = []
            return lista_
        else:
            lista_ = json.loads(json_string)
            return lista_

    @classmethod
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

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes a list of Rectangles/Squares in csv"""
        filename = cls.__name__ + ".csv"
        l = []
        try:
            with open(filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for args in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(args[0]),
                                      "width": int(args[1]),
                                      "height": int(args[2]),
                                      "x": int(args[3]),
                                      "y": int(args[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(args[0]), "size": int(args[1]),
                                      "x": int(args[2]), "y": int(args[3])}
                    obj = cls.create(**dictionary)
                    l.append(obj)
        except:
            pass
        return l
