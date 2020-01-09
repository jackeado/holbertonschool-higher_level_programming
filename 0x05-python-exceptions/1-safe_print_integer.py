#!/usr/bin/python3
'''
function that prints x elements of a list
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(True)
    except(ValueError, TypeError):
        return(False)
