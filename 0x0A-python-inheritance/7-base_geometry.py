#!/usr/bin/python3
"""
This module has a class BaseGometry with two public instance
attributes
"""


class BaseGeometry:
    """
    The BaseGeometry class
    """
    def area(self):
        """
        The area public instance attribute that raise an
        exception if value is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        The public instance attribute that validates the input
        to ensure that the input is an integer and is greater than
        zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
