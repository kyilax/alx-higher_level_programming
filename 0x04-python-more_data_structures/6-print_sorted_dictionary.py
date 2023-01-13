#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    b = sorted(a_dictionary.items())
    for k, v in b:
        print(k, v, sep=": ")
