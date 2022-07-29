#!/usr/bin/python3
"""appends to a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends to a string at the end of a text file"""
    with open(filename, 'a+') as f:
        return f.write(text)
