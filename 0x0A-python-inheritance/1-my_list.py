#!/usr/bin/python3

class MyList(list):
    """Inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
