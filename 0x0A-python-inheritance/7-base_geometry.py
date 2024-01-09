#!/usr/bin/python3

class BaseGeometry:
    """
    Class representing the base geometry
    with an integer_validator method.
    """

    def integer_validator(self, name, value):
        """Validates the value as a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
