#!/usr/bin/python3
"""
This module defines a function that converts a JSON string
into a Python object.
"""
import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: The JSON string to be deserialized.

    Returns:
        any: The Python object represented by the JSON string.
    """
    # json.loads() takes a string and converts it back into
    # a Python object (list, dict, etc.)
    return json.loads(my_str)
