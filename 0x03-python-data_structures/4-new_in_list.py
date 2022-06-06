#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    arr_len = len(my_list) - 1
    copy_arr = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > arr_len:
        return my_list
    else:
        copy_arr[idx] = element
        return copy_arr
