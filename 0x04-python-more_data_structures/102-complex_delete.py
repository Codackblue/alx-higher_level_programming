#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    f_keys = list(a_dictionary.keys())

    for fvalue_dic in f_keys:
        if value == a_dictionary.get(fvalue_dic):
            del a_dictionary[fvalue_dic]

    return (a_dictionary)
