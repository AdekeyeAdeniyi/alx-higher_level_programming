#!/usr/bin/python3

def find_peak(list_of_integers):
    """
        Function that finds a peak in a list of unsorted integer
        ---------------------------------------------

        Argument
        ---------
        list_of_integers: list
            unsorted list

    """

    if list_of_integers:
        return max(list_of_integers)
    else:
        return "None"
