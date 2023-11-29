#!/usr/bin/python3

def remove_char_at(fstr, fn):
    if fn < 0:
        return (fstr)
    return (fstr[:fn] + fstr[fn+1:])
