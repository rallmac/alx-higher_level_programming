#!/usr/bin/python3
"""
This module inherits the base geometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class that inherits BaseGeometry """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ The public instance attribute of area """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the width and height description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
