#!/usr/bin/python3
"""
This Class inherits from list
"""


class MyList(list):
    """ This is the list class to inherit """
    def print_sorted(self):
        """ This attribite inherits from the class """
        sorted_list = sorted(self)
        print(sorted_list)
