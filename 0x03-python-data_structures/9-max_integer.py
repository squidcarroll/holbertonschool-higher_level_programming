#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        m = my_list[0]
        for x in my_list:
            if x > m:
                m = x
        return m
