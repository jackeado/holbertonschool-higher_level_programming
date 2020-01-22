#!/usr/bin/python3
import json
"""
Cotains read file function
"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
