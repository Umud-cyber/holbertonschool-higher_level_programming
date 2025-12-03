#!/usr/bin/python3
"""Convert CSV data to JSON file."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON and save into data.json."""
    try:
        data_list = []

        with open(csv_filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False
