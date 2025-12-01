#!/usr/bin/python3
"""
Module that defines a subclass of list with a method
to print the list sorted in ascending order.
"""


class MyList(list):
    """A subclass of list that provides a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
