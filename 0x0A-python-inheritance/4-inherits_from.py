#!/usr/bin/python3
"""
This module returns true if an object is an instance
if a class inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that is inherited (directly or indirectly) from the specified
    class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
