#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ''
    num = 0
    for i in str:
        if num != n:
            strcpy += i
        else:
            strcpy += ' '
        num += 1
    return strcpy
