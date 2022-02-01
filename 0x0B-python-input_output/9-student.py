#!/usr/bin/python3
"""
Modulus with class Student
"""


class Student:
    """
    Class Student with first name, last and age
    """
    def __init__(self, first_name, last_name, age):
        """
        Function that init
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function that retrieves a dictionary
        representation of a Student
        """
        return self.__dict__
