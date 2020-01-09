#!/usr/bin/python3
'''
function that prints x elements of a list
'''

def safe_print_list(my_list=[], x=0):
    counter = 0
    for c in range(x):
        try:
            print(my_list(c), end="")
            counter += 1
        except IndexError:
            break
    print()
    return(counter)
