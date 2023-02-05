#!/usr/bin/python3
""" a module that add an integer"""

def add_integer(a, b=98):
    """ addition of integers """

    if not int(a) or not float(a):
        return "a must be an integer"
    elif not int(b) or not float(b):
        return "b must be an integer"
    else:
        a = int(a)
        b = int(b)
        return (a + b)
