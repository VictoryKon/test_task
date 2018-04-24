"""Validation module."""

from trafaret import DataError
from fetch_data.logic import exceptions
from fetch_data.logic import trafaret_schema


def validate(line):
    """Validate line data.

    Args:
        line (dict): one line data.

    Returns:
        dict: validated line data. Raises DataValidationFailed Exception if the
        validation fails.
    """
    try:
        validated_data = trafaret_schema.ADDRESS_DATA_SCHEMA.check(line)
        return validated_data
    except DataError as e:
        trafaret_error = e.error
        invalid_fields = [field for field in trafaret_error]
        raise exceptions.DataValidationFailed(invalid_fields)
