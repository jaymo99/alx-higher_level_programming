#!/usr/bin/python3
""" This module creates a Rectangle class.
"""


class Rectangle():
    """Represents a Rectangle

    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle

    Attributes:
        number_of_instances (int): The number of active Rectangle instances
        print_symbol: Used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ("")
        for row in range(self.__height):
            for col in range(self.__width):
                rect.append(str(self.print_symbol))

            # add newline to all lines except the last one
            if row < (self.__height - 1):
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

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

        perimeter = 0
        if self.__width != 0 and self.__height != 0:
            perimeter = (self.__width + self.__height) * 2

        return perimeter

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle instances based on area

        Args:
            rect_1: first Rectangle
            rect_2: second Rectangle

        Returns:
            The biggest rectangle based on the area.
            OR 'rect_1' if both have the same area value
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Creates a square. All sides are equal

        Args:
            size: width/length of the square

        Returns:
            A new Rectangle instance with width == height == size
        """

        return (Rectangle(size, size))
