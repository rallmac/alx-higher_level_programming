#!/usr/bin/python3
"""
defines a text file-reading function
"""

def read_file(filename=""):
    """
    Print the contents of a UTF8 text file to stdoutput
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
