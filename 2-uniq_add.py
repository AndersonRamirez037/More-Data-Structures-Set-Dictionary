#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    temp = 0
    for i in my_list:
        if i > temp:
            temp = i
            sum += temp
    return sum