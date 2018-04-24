import json
import urllib.parse
import urllib.request

import requests

fetch_xml_url = 'http://0.0.0.0:5000/initial_data?'
fetch_xml_values = (
    ('filename', 'File1.txt'),
    ('filename', 'File2.txt'),
    ('filename', 'File3.txt'))

write_data_url = 'http://0.0.0.0:5555/xml_result'


def main():
    """Main controller function, controls the microservices interaction flow.

    Returns:
        str: filename.
    """
    xml_get_result = get_xml()
    if isinstance(xml_get_result, urllib.error.HTTPError):
        return
    xml_save_result = put_xml(xml_get_result)
    if isinstance(xml_save_result, urllib.error.HTTPError):
        return
    print(xml_save_result)
    return xml_save_result


def get_xml():
    """Fetch xml from fetch_xml service.

    Returns:
        dict: XML string.
    """
    try:
        url_params = urllib.parse.urlencode(fetch_xml_values)
        request = urllib.request.Request(fetch_xml_url + url_params)
        response = urllib.request.urlopen(request)
        result = binary_to_dict(response.read())
        return result
    except urllib.error.HTTPError as e:
        print(e)
        return e


def put_xml(xml_str_to_save):
    """Perform PUT request to write_data microservice to save XML.

    Args:
        xml_str_to_save (dict): dict containing XML string to write to file.

    Returns:
        str: filename.
    """
    try:
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps(xml_str_to_save).encode('utf8')
        request = urllib.request.Request(
            url=write_data_url, data=payload,
            method='PUT', headers=headers)
        response = urllib.request.urlopen(request)
        result = binary_to_dict(response.read())
        return result
    except urllib.error.HTTPError as e:
        print(e)
        return e


def binary_to_dict(binary_data):
    """Convert binary data to dictionary.

    Args:
        binary_data (binary): data to convert.

    Returns:
        dict: data converted to dict.
    """
    decoded_res = binary_data.decode('ascii')
    result = json.loads(decoded_res)
    return result


if __name__ == '__main__':
    main()
