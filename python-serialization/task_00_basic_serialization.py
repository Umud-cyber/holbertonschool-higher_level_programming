#!/usr/bin/python3
"""jdf hdszjb   
fjk vxdfjn    lsfdjmfd"""


import json


def serialize_and_save_to_file(data, filename):
    """ szdjkj sdfkjs"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)
        
def load_and_deserialize(filename):
    """ jdb sdj s ds """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
