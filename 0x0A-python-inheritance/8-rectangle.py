#!/usr/bin/python3
""" Base Geometry Class """


class BaseGeometry:
    """ class that improve geometry with integer validator"""
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if (type(value) is not int):
            raise TypeError(name + " must be an integer")
        if (value <= 0):
            raise ValueError(name + " must be greater than 0")


""" Program that creates a Rectangle and intance its values """


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height