#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""
from sys import argv

save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    jsonList = load_from_json_file(filename)
except Exception:
    jsonList = []

for arg in argv[1:]:
    jsonList.append(arg)
save_to_json_file(jsonList, filename)
