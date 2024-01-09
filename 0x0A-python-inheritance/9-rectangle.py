#!/usr/bin/python3

class Rectangle(BaseGeometry):
    """Class representing a rectangle with width and height."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance with width and height."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
