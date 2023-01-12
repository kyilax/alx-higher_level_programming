#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = my_list.copy()
    idx = new_lst.index(search)
    new_lst[idx] = replace
    return new_lst
