#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for frow in matrix:
        for fcol in frow:
            print("{:d}".format(fcol), end=" " if fcol != frow[-1] else "")
        print()
