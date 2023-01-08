#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    mlist = my_list[0]
    for i in my_list:
        if i >= mlist:
            mlist = i
    return mlist
