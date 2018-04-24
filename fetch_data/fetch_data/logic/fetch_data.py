"""Main logic module which controls the execution flow."""

from os.path import abspath
from os.path import dirname
from os.path import join

from fetch_data import config
from fetch_data.logic import exceptions
from fetch_data.logic import read_from_file
from fetch_data.logic import transform_data
from fetch_data.logic import validation

import logging
logfile = logging.getLogger()


@exceptions.log_exception
def process_files(filenames):
    """Collect data from files, run validation and compose XML string.

    Returns:
        dict: formatted XML string.
    """
    data_from_files = []
    for file in filenames:
        file_name_in_dir = join(config.FILE_DIR, file)
        file_path = abspath(
            join(dirname(dirname(dirname(__file__))), file_name_in_dir))
        data_from_file = read_from_file.read_data(file_path)
        data_from_files.extend(data_from_file)

    valid_lines = []
    for line in data_from_files:
        try:
            valid_line = validation.validate(line)
            valid_lines.append(valid_line)
        except exceptions.DataValidationFailed as e:
            logfile.debug(e)
            pass
    xml_result = transform_data.data_to_xml(valid_lines)
    return xml_result
