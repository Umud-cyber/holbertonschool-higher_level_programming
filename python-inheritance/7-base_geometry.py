#!/usr/bin/python3
"""
BaseGeometry class
"""

class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates 'value' as a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
