#!/usr/bin/python3
""" dhd jhjdf djf"""

class Student():
    """ jfdfd jxdfgbkx"""


    def __init__(self, first_name, last_name, age):
        """ sjkdd fzhjf """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """ dnzf """
        return self.__dict__
    if type(attrs) is list:
        new = {}
        for key in attrs:
            if key in self.__dict__:
                new[key] = self.__dict__[key]
        return new
