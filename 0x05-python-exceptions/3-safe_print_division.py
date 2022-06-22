#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        temp = a / b
    except ZeroDivisionError:
        temp = None
    finally:
        print("Inside result: {}".format(temp))
    return temp
