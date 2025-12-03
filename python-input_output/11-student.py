#!/usr/bin/python3
"""Module that defines a Student class with JSON helpers."""

class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of the Student.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            new = {}
            for key in attrs:
                if hasattr(self, key):
                    new[key] = getattr(self, key)
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
