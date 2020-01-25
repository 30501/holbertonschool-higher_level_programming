#!/usr/bin/python3
""" First Rectangle that inherits from Base """
from . base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class Constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Retriebe the width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set passet private attribute of width """
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set passed private attribute of height """
        self.__height = value

    @property
    def x(self):
        """ Retrieve private instance attribute x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ set private instance attribute x """
        self.__x = value

    @property
    def y(self):
        """ Retrieve private instance sttribute y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ set private instance attribute y """
        self.__y = value
