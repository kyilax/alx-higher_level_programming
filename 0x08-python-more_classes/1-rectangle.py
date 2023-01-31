#!/usr/bin/python3
"""
deines a class rectangle
"""


class Rectangle:
    """a class rect"""
    def int(self, width=0, height=0):
        """ intializes the rect"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the value of width """
        if type(value) not int(value):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ gets the value of height"""
        return self.__width

    @height.setter
    def height(self, value):
        """ set the value of width """
        if value not int(value):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value
