#!/usr/bin/python3
""" This module contains the rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A subclass that represents a rectangle """
    def __init__(self, size):
        """ The init constructor """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        This method is a string representation of a square
        and returns area of the square
        """
        return "[square] {}/{}".format(self.__size, self.__size)
