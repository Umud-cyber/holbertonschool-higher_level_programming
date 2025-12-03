#!/usr/bin/python3
"""Basic JSON serialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save to file."""
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from file and deserialize to dictionary."""
    with open(filename, "r") as f:
        return json.load(f)
