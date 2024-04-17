#!/usr/bin/python3
"""
Define a python class-to-JSON function
"""

def class_to_json(obj):
    """
    Return the dictionary representation of a simple data structure
    """
    return obj.__dict__
