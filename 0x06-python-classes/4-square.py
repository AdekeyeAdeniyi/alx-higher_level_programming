#!/usr/bin/python3
""" Module contain: Square Class"""


class Square:
    """
        Square: Defines a Square
        Atrributes:
            size
        Methods:
            __init__
    """
    def __init__(self, size=0):
        """
            Intializing size atrribute for every Square instance
            Args:
                Size: (type integer)
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
            Area: Method that return the area of a square instance
        """
        result = self.__size * self.__size
        return result

    @property
    def size(self):
        """
            getter method for private field size
            Return:
                size of square
        """
        return self.__size

    @property
    def size(self, value):
        """
            setter method for private field size
            Args:
                value (int): value to be set
            Return:
                nothing
        """
        if not (isinstance(value, int)):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
