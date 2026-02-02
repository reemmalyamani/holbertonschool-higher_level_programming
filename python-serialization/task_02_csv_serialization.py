#!/usr/bin/env python3
"""
Task 02: CSV serialization utilities.

Assumes `data` is a list of dictionaries (rows).
Provides:
- serialize_and_save_to_file(data, filename)
- load_and_deserialize(filename)

Returns: list[dict]
"""

import csv


def serialize_and_save_to_file(data, filename):
    """
    Write list of dicts to CSV file.
    Replaces the file if it already exists.

    Example:
    data = [{"name": "John", "age": 30}, {"name": "Sara", "age": 25}]
    """
    if not data:
        # Create an empty file (no headers) if data is empty
        open(filename, "w", newline="", encoding="utf-8").close()
        return

    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise TypeError("data must be a list of dictionaries for CSV serialization")

    # Use union of keys to avoid missing columns
    fieldnames = []
    seen = set()
    for row in data:
        for k in row.keys():
            if k not in seen:
                seen.add(k)
                fieldnames.append(k)

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def load_and_deserialize(filename):
    """
    Read CSV file and return list of dicts.
    All values come back as strings (CSV has no native types).
    """
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]
