#!/usr/bin/python3
"""defines a file-writing function"""

def write_file(filename="", text=""):
    """write a string to UTF8 text file
    Args:
        filename (str): the name of the file to write
        text (str): the next to write to the file
    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
