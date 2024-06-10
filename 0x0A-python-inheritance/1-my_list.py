#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class includes an additional method to print the
    elements of the list in a sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in a sorted order.

        This method sorts the list in ascending order and
        prints the sorted list.

        Example:
            >>> my_list = MyList([3, 1, 2])
            >>> my_list.print_sorted()
            [1, 2, 3]
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

