#!/usr/bin/python3
"""
This module defines a function that adds attributes to
Objects
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object where possible
    Args:
            obj (any): The to add attribute to
            att (str): The name of attribute to add obj to
            value (any): The value of the attribute
    Raises:
            TypeError: if attribute is None
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
