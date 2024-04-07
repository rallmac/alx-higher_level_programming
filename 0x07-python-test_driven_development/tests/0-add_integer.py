#!/usr/bin/python3
"""Define the function that adds two integers"""

def add_integer(a, b=98):
    """Check if both inputs are integers or floats"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a, must be an integer or b must be an integer")

    """Cast to integers if inputs are floats"""
    a = int(a)
    b = int(b)

    """Return the addition of a and b"""
    return (a + b)
