#!/usr/bin/python3

class Square(Rectangle):
    """Class representing a square with a size."""

    def __init__(self, size):
        """Initializes a Square instance with size."""
        super().__init__(size, size)
