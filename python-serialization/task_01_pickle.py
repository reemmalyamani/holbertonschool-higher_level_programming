#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError, OSError):
            return None

        return None
