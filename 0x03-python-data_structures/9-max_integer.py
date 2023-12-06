#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        fmax = my_list[0]
        for f in range(len(my_list)):
            if my_list[f] > fmax:
                fmax = my_list[f]
        return fmax
