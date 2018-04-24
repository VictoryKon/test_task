"""Main logic module."""

from os.path import abspath
from os.path import dirname
from os.path import join

from datetime import datetime

from write_data import config
from write_data.logic import exceptions


@exceptions.log_exception
def write_xml_to_file(xml_str_to_write):
    """Write the given XML string to file.

    Args:
        xml_str_to_write (str): XML string to write to file.

    Returns:
        str: filename.
    """
    file_name = compose_filename()
    with open(file_name, 'w') as file_to_write:
        file_to_write.write(xml_str_to_write)
    return file_name


@exceptions.log_exception
def compose_filename():
    """Compose file name.

    File name is composed from current UTC date and time.

    Returns:
        str: file name.
    """
    formatted_utc_now = datetime.utcnow().strftime('%B_%d_%Y-%H:%M:%S')
    file_name = ''.join([formatted_utc_now, config.TXT_FILE_EXTENSION])
    file_name_in_dir = join(config.SAVED_XML_FILES_DIR, file_name)
    file_path = abspath(
        join(dirname(dirname(dirname(__file__))), file_name_in_dir))
    return file_path
