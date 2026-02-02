#!/usr/bin/env python3
"""
Task 01: Pickle serialization utilities.

Provides:
- serialize_and_save_to_file(data, filename)
- load_and_deserialize(filename)

Pickle is Python-specific and not safe for untrusted files.
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serialize `data` (any picklable Python object) and save to `filename`.
    If the file exists, it will be replaced.
    """
    with open(filename, "wb") as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)


def load_and_deserialize(filename):
    """
    Load pickled data from `filename` and return the deserialized object.
    """
    with open(filename, "rb") as f:
        return pickle.load(f)
