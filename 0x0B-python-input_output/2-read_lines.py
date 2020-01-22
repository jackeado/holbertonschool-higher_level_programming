#!/usr/bin/python3
"""
Cotains read file function
"""


def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for li in lines:
                print(li, end='')
        else:
            for i in range(nb_lines):
                print(lines[i], end='')
