#!/usr/bin/python3
"""
Module that prints text with indentation
"""


def text_indentation(text):
    """
    Prints text with two new lines after ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in ".?:":
        text = text.replace(c, c + "\n\n")

    lines = text.split("\n")
    for line in lines:
        print(line.strip())

