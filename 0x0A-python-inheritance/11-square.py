#!/usr/bin/python3
""" This module contains a rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A rectancle subclass """
    def __init__(self, size):
        """ The init method """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of a square
        and a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
