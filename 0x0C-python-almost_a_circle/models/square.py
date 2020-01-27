#!/usr/bin/python3
"""

"""
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if len(args):
            for arg, attr in enumerate(args):
                if arg == 0:
                    self.id = attr
                if arg == 1:
                    self.size = attr
                if arg == 2:
                    self.x = attr
                if arg == 3:
                    self.y = attr
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
