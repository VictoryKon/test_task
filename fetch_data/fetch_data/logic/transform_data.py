"""Module containing logic layer for data transformation."""

import xml.etree.cElementTree as ElementTree

from fetch_data.logic import exceptions


@exceptions.log_exception
def data_to_xml(data):
    """Convert data to XML of predefined format.

    XML contains <root> element and <address> subelements in it, each address
    subelement contains data from one address line.

    Args:
        data (list): data to build an XML tree. Is a list of dicts.

    Returns:
        str: formatted XML string.
    """
    root = ElementTree.Element('root')
    for line in data:
        xml_address_element = ElementTree.SubElement(root, 'address')
        for key in line:
            ElementTree.SubElement(xml_address_element, key).text = (
                str(line[key]))
    result_string = ElementTree.tostring(root).decode()
    return result_string
