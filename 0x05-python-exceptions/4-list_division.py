#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            tmp_result = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("wrong type")
            tmp_result = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp_result = 0
        except IndexError:
            print("Out of range")
            tmp_result = 0
        finally:
            new_list.append(tmp_result)
    return new_list
