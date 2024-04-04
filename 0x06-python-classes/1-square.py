#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the width of the square."""
        return self.__size

    @width.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def height(self):
        """Get/set the height of the square."""
        return self.__height
