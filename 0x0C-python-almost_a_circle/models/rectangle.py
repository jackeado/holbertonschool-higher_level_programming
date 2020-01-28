#!/usr/bin/python3
"""
contains rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Initialize the base Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of widht"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of widht"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Display a Rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.width)

    def __str__(self):
        """informal string representation of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """updates multiple attributes"""
        if len(args):
            for arg, asig in enumerate(args):
                """ "enumerate" adds counter to an iterable and returns it"""
                if arg == 0:
                    self.id = asig
                elif arg == 1:
                    self.width = asig
                elif arg == 2:
                    self.height = asig
                elif arg == 3:
                    self.x = asig
                elif arg == 4:
                    self.y = asig
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
