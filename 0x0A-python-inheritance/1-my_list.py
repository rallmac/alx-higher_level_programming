#!/usr/bin/python3
"""
This Class inherits from list
"""


class MyList(list):
""" This is the list class to inherit """
    def print_sorted(self):
        pass
        """ This attribite inherits from class """
        sorted_list = sorted(self)
        print(sorted_list)
