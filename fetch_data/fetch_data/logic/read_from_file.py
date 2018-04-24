"""Module representing logic for reading data from file"""

import csv

from fetch_data.logic import exceptions


@exceptions.log_exception
def read_data(file_path):
    """Read data from file.

    Args:
        file_path (str): path to file that should be read.

    Returns:
        list: data from file, list of dicts each representing the line
        in a file.
    """
    with open(file_path, 'r') as file_to_read:
        csv_reader = csv.reader(file_to_read, delimiter=';')
        result = []
        for row in csv_reader:
            row_data = {}
            for entity in row:
                key, val = entity.split('=')
                row_data.update({key: val})
            result.append(row_data)
    return result
