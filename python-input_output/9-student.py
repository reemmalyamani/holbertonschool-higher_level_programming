#!/usr/bin/python3
"""Define a Student class with JSON serialization."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance."""
        return self.__dict__
