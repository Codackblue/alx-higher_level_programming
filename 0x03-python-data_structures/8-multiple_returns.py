#!/usr/bin/python3
def multiple_returns(sentence):
    fmy_tuple = ()
    if len(sentence) == 0:
        fmy_tuple = 0, "None"
    else:
        fmy_tuple = len(sentence), sentence[0]
    return fmy_tuple
