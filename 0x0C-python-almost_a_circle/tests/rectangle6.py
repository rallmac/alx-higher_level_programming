#!/usr/bin/python3

from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if isinstance(width, int) and width > 0:
            self.__width = width
        elif not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
            raise ValueError("width must be > 0")

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if isinstance(height, int) and height > 0:
            self.__height = height
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        else:
            raise ValueError("height must be > 0")

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, int) and x >= 0:
            self.__x = x
        elif not isinstance(x, int):
            raise TypeError("x must be an integer")
        else:
            raise ValueError("x must be >= 0")

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if isinstance(y, int) and y >= 0:
            self.__y = y
        elif not isinstance(y, int):
            raise TypeError("y must be an integer")
        else:
            raise ValueError("y must be >= 0")

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args):
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.set_width(args[1])
        if len(args) >= 3:
            self.set_height(args[2])
        if len(args) >= 4:
            self.set_x(args[3])
        if len(args) >= 5:
            self.set_y(args[4])

    def __str__(self):
        return(f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}')
