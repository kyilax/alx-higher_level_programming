#!/usr/bin/python3
def best_score(a_dictionary):
    c = 0
    a = ""
    if not a_dictionary.values():
        return None
    else:
        for k, v in a_dictionary.items():
            if v > 0:
                c = v
                a = k
    return a
