#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        p = fct(*args)
        return p
    except Exception as error:
        print("Exeption: {}".format(error), file=sys.stderr)
        return None
