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

    def to_json(self, attrs=None):
        """
        Function that retrieves a dictionary
        representation of a Student
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        else:
            retorno = {}
            for x in attrs:
                if type(x) is not str:
                    return self.__dict__
                if x in self.__dict__.keys():
                    retorno[x] = self.__dict__[x]
            return retorno
