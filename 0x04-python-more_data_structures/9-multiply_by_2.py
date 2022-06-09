#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    new_keys = new_dict.keys()
    for key in new_keys:
        new_dict[key] *= 2
        
    print(new_dict)
