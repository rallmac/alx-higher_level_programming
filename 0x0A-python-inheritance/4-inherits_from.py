#!/usr/bin/python3
"""
This module returns true if an object is an instance
if a class inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    The function of that inherits from a class
    """
    obj_class = type(obj)

    if obj_class == a_class:
        return True

    for base_class in obj_class.__bases__:
        if inherits_from(base_class, a_class):
            return True

    return False
