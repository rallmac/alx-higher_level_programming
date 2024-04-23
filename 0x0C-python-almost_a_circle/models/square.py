#!/usr/bin/python3

from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f'[Square] ({self.id}) {self.get_x()}/{self.get_y()} - {self.get_width()}')

    def get_size(self):
        return (self.get_width())
    
    def set_size(self, size):
        self.set_width(size)
        self.set_height(size)

    size = property(get_size, set_size)