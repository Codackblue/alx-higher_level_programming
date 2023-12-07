#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    f_dict = {}
    for key, value in a_dictionary.items():
        f_dict.update({key: (value * 2)})
    return f_dict
