#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = my_list.copy()
    new_lst[search] = replace
    return new_lst
