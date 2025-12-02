#!/usr/bin/python3
"""Defines a Square class based on Rectangle (task 10-square)."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize a Square with validated private size"""

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
