#!/usr/bin/python3
"""
Contians a class Mylist
"""


class MyList(list):
    '''Represents a class Mylist'''
    def __init__(self):
        """initializing class"""
        super().__init__()

    def print_sorted(self):
        """method print sorted"""
        print(sorted(self))
