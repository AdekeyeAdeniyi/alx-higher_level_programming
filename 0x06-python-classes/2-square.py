#!/usr/bin/python3

""" Module contains: Square Class"""


class Square:
    """
        Square Class: defines a square
        Atrributes:
            size
        Methods:
            __init__
    """
    def __init__(self, size=0):
        """
            Intialization of atrributes for every instance
            Args:
                size: (private field)
        """
        if(isinstance(size, int)):
            """
                Checking if size value is an integer greater than or equal to
                zero
            """
            if(size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
