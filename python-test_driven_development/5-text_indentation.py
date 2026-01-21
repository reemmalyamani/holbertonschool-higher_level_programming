#!/usr/bin/python3
"""Module that prints text with indentation"""


def text_indentation(text):
    """Prints text with two new lines after '.', '?' and ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
