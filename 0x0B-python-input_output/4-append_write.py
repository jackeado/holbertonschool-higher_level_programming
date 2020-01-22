#!/usr/bin/python3
"""
Cotains read file function
"""


def append_write(filename="", text=""):
    with open(filename, encoding='utf-8', mode='a') as f:
        char = f.write(text)
        return char
