#!/usr/bin/python3
"""Convert an instance to a JSON-serializable dictionary."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object."""
    return obj.__dict__
