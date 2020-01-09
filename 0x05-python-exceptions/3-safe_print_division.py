#!/usr/bin/python3
'''
function that prints x elements of a list
'''


def safe_print_division(a, b):
    try:
        c = a/b
    except (ZeroDivisionError, IndexError):
        c = None
    finally:
        print("Inside result: {}".format(c))
    return c
