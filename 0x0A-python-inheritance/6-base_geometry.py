#!/usr/bin/python3
"""
This module contains the class defination of BaseGeometry
"""


class BaseGeometry:
    """
    The BaseGeometry class with the area method that
    raise exception with a message (Area is not implemented)
    """
    def area(self):
        raise Exception("area() is not implemented")
