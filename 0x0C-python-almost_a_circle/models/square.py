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

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.get_width(),
            'x': self.get_x(),
            'y': self.get_y()
        }

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.set_size(args[1])
            if len(args) >= 3:
                self.set_x(args[2])
            if len(args) >= 4:
                self.set_y(args[3])
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.set_size(value)
                elif key == 'x':
                    self.set_x(value)
                elif key == 'y':
                    self.set_y(value)