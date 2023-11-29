#!/usr/bin/python3

for digitf1 in range(0, 10):
    for digitf2 in range(digitf1 + 1, 10):
        if digitf1 == 8 and digitf2 == 9:
            print("{}{}".format(digitf1, digitf2))
        else:
            print("{}{}".format(digitf1, digitf2), end=", ")
