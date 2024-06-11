#!/usr/bin/python3
"""
This module contains a class Rectangle with an initialitation
attribute. The rectangle class inherits the BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """
    The rectangle class that inherits the BaseGeometry
    """
    def __init__(self, width, height):
        """
        The init method. In this method, the width is a private
        and the height is only positive integer
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
