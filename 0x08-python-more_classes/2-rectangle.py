#!/usr/bin/python3
""" This module creates a Rectangle class.
"""


class Rectangle():
    """Represents a Rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width of rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height of rectangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle

        Returns:
            int: The area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of a rectangle

        Returns:
            int: The perimeter of the rectangle
        """

        return (self.__width + self.__height) * 2
