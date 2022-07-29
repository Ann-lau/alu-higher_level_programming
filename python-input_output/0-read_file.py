#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """read file"""
    with open('filename', encoding="UTF8") as f:
        read_data = f.read()
        print (read_data, end="")
