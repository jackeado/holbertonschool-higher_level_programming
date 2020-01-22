#!/usr/bin/python3
import json
"""
Cotains read file function
"""


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”"""
    with open(filename, encoding='utf-8', mode='r') as json_file:
        return json.load(json_file)
