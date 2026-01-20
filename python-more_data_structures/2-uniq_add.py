#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for n in set(my_list):
        total += n
    return total
