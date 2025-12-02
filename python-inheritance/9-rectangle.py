#!/usr/bin/python3
""" fkdf jf"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """ fjjf jfnf dkf"""
        self.integer_validator("width", width)
        self.__width

        self.integer_validator("height", height)
        self.__height

        def area():
            """ Jdhhd idjhfk djkj"""
            return self.__width * self.__height
        def __str__(self):
            """ nfhf jfjfjfdn  jdfjjf"""
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
