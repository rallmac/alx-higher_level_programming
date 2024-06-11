#!/usr/bin/python3
""" This module contains a class MyInt """


class MyInt(int):
    """ Another version of an integer """
    def __eq__(self, other):
        """ changing the value of != to == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ changing the value of == to != """
        return super().__eq__(other)
