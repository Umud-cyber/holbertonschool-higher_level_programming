#!/usr/bin/python3
"""
Rectangle class inheriting from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize width and height after validation"""

        # validate inputs using parent method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # set private attributes
        self.__width = width
        self.__height = height
