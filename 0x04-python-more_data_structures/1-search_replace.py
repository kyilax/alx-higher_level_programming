#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    elif search >= len(my_list):
        return
    else:
        new_lst = my_list.copy()
        idx = new_lst.index(search)
        new_lst[idx] = replace
        return new_lst
