#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if (len(my_list_1) != len(my_list_2)):
        print("out of range")
    p = []
    for i in range(len(my_list_1)):
        result = 0
        try:
            result (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            p.append(result)
    return p
