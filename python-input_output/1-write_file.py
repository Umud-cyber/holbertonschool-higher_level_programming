#!/usr/bin/python3
"""Module that defines a function to write text to a UTF-8 file."""

def write_file(filename="", text=""):
    """Writes text to a file and returns number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
