#!/usr/bin/python3
"""
Contains class Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initialize the base Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ returns string dictionary"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                                                     self.id,
                                                     self.x,
                                                     self.y,
                                                     self.width)

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
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
        """to dictionary representation"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
