#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    arr_len = len(my_list) - 1
    if idx < 0:
        return (my_list)
    elif idx > arr_len:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
