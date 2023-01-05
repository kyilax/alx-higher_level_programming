#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    strcpy = ''
    num = 0
    for i in str:
        if num != n:
            strcpy += i
        num += 1
    return strcpy
