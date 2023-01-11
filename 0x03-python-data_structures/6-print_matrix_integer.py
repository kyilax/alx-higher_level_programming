#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        ilen = len(i)
        h = 0
        for j in i:
            if h == 0:
                print("{:d}".format(j), end="")
            else:
                print(" {:d}".format(j), end="")
            h += 1
        print()
