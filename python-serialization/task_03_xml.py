#!/usr/bin/env python3
"""
Task 03: XML serialization utilities.

Serializes a Python dictionary to XML and back.
Supports: dict, list, str, int, float, bool, None.

Provides:
- serialize_and_save_to_file(data, filename)
- load_and_deserialize(filename)

Returns: dict
"""

import xml.etree.ElementTree as ET


def _to_xml(parent, key, value):
    elem = ET.SubElement(parent, "item", key=str(key))

    if value is None:
        elem.set("type", "none")
        elem.text = ""
    elif isinstance(value, bool):
        elem.set("type", "bool")
        elem.text = "true" if value else "false"
    elif isinstance(value, int):
        elem.set("type", "int")
        elem.text = str(value)
    elif isinstance(value, float):
        elem.set("type", "float")
        elem.text = str(value)
    elif isinstance(value, str):
        elem.set("type", "str")
        elem.text = value
    elif isinstance(value, list):
        elem.set("type", "list")
        for i, v in enumerate(value):
            _to_xml(elem, i, v)
    elif isinstance(value, dict):
        elem.set("type", "dict")
        for k, v in value.items():
            _to_xml(elem, k, v)
    else:
        raise TypeError(f"Unsupported type for XML serialization: {type(value)}")


def _from_xml_item(elem):
    t = elem.get("type")
    key = elem.get("key")

    if t == "none":
        return key, None
    if t == "bool":
        return key, (elem.text == "true")
    if t == "int":
        return key, int(elem.text) if elem.text else 0
    if t == "float":
        return key, float(elem.text) if elem.text else 0.0
    if t == "str":
        return key, elem.text or ""
    if t == "list":
        items = []
        for child in elem.findall("item"):
            _, v = _from_xml_item(child)
            items.append(v)
        return key, items
    if t == "dict":
        d = {}
        for child in elem.findall("item"):
            ck, cv = _from_xml_item(child)
            d[ck] = cv
        return key, d

    raise ValueError(f"Unknown XML item type: {t}")


def serialize_and_save_to_file(data, filename):
    """
    Serialize dictionary `data` into an XML file.
    Replaces the file if it already exists.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary for XML serialization")

    root = ET.Element("root")
    for k, v in data.items():
        _to_xml(root, k, v)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def load_and_deserialize(filename):
    """
    Load XML file and deserialize into a dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for item in root.findall("item"):
        k, v = _from_xml_item(item)
        result[k] = v
    return result
