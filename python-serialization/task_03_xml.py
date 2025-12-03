#!/usr/bin/python3
"""XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save to file."""
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as XML children
        for key, value in dictionary.items():
            item = ET.SubElement(root, key)
            item.text = str(value)

        # Write to file
        tree = ET.ElementTree(root)
        tree.write(filename)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML data back into a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            text = child.text

            # Attempt automatic type conversion
            if text is None:
                result[child.tag] = None
            else:
                # Try int
                if text.isdigit():
                    result[child.tag] = int(text)
                # Try bool
                elif text.lower() == "true":
                    result[child.tag] = True
                elif text.lower() == "false":
                    result[child.tag] = False
                else:
                    # Default: string
                    result[child.tag] = text

        return result

    except Exception:
        return None
