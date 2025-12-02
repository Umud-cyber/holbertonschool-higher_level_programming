#!/usr/bin/python3
"""Module thatction to write a string to a text file (UTF-8)."""
  

def write_file(filename="", text=""):
    """Writthe number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
