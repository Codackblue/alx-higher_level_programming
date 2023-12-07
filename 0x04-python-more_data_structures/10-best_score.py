#!/usr/bin/python3

def best_score(a_dictionary):
    """
    A function that returns a key with the biggest value.
    """
    if a_dictionary:
        f_list = list(a_dictionary.keys())
        fscore = 0
        fleader = ""
        for f in f_list:
            if a_dictionary[f] > fscore:
                fscore = a_dictionary[f]
                fleader = f
        return fleader
