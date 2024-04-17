#!/usr/bin/python3
"""
defines a class student
"""

class Student:
    """
    represent a student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        get a dictionary representation of the student
        if attrs is list of srings, represents only those attributes
        included in the list
        Args:
            attrs (list): (Optional) the attributes to represent
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
