#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list once for each integer
    """
    f_list = []
    fsum = 0
    for f in my_list:
        if f not in f_list:
            fsum += f
            f_list.append(f)
    return fsum
