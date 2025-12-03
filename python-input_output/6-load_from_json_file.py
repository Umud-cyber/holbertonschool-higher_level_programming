#!/usr/bin/python3
""" skwjd fjefksn rjk"""
import json


def load_from_json_file(filename):
    """ fjs srjgr guisljks"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
