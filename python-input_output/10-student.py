#!/usr/bin/python3
"""Defines a simple Student class."""


class Student:
    """Student model."""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the student."""
        if type(attrs) is list:
            new_dict = {}
            for key in attrs:
                if type(key) is str and key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__
