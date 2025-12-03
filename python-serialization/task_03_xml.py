#!/usr/bin/python3
"""XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save to file."""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            item = ET.SubElement(root, key)
            item.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)

        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML into a Python dictionary (all values as strings)."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            # Just return text as string (NO type conversion)
            result[child.tag] = child.text

        return result
    except Exception:
        return None
