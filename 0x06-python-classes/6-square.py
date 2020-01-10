#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
       Attributes:
           __size (int): size of a side of the square
       """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
              Args:
                  size (int): size of a side of the square
              Returns: None
              """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
                Returns:
                    The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
               Args:
                   value (int): the size of a size of the square
               Returns:
                   None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) != tuple or
                len(position) != 2 or
                type(position[0]) != int or
                type(position[1]) != int or
                position[0] < 0 or
                position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for p in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(" ", end="")
                else:
                    print("#", end="")
            print()
