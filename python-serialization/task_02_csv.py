#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and save it to data.json.

    Returns True if successful, False otherwise.
    """
    try:
        data = []

        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, PermissionError, OSError):
        return False
