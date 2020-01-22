#!/usr/bin/python3
"""
Cotains read file function
"""


def number_of_lines(filename=""):
    c_lines = 0
    with open(filename, encoding='utf-8') as f:
        for lines in f:
            c_lines += 1
        return (c_lines)
