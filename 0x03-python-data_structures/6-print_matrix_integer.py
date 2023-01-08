#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        ilen = len(i)
        for j in i:
            print(" {}".format(j), end="")
        print()
