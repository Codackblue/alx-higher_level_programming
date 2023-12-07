#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary ordered by keys
    """
    fkeys = list(a_dictionary.keys())
    fkeys.sort()
    for fkey in fkeys:
        print("{}: {}".format(fkey, a_dictionary[fkey]))
