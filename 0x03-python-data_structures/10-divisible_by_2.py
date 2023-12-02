#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    fnew_list = []
    for f in range(len(my_list)):
        if my_list[f] % 2 == 0:
            fnew_list.append(True)
        else:
            fnew_list.append(False)
    return fnew_list
