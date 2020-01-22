#!/usr/bin/python3
"""
Cotains read file function
"""


def write_file(filename="", text=""):
    with open(filename, encoding='utf-8', mode='w') as f:
        ch = f.write(text)
        return ch
