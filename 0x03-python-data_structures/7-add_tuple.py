#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    fnew_tuple = ()
    ftuple_1 = tuple_a + (0, 0)
    ftuple_2 = tuple_b + (0, 0)
    fnew_tuple = ftuple_1[0] + ftuple_2[0], ftuple_1[1] + ftuple_2[1]
    return fnew_tuple
