#!/usr/bin/python3
""" Program that defines a Square in base from Rectangle """
from . rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overriding the __str__ method that returns a custom string """
        mssg = "[Square] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)
        return (mssg)
