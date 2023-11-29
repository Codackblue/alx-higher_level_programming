#!/usr/bin/python3

def magic_calculation(fa, fb, fc):
    """Match bytecode provided."""
    if fa < fb:
        return (fc)
    if fc > fb:
        return (fa + fb)
    return (fa*fb - fc)
