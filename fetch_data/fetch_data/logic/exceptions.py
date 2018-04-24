"""Custom Exceptions module."""

import functools

import logging
logfile = logging.getLogger(__name__)


class DataValidationFailed(Exception):
    """Exception raises if data validation failed."""

    invalid_fields = None

    def __init__(self, invalid_fields):
        """Show exception message."""
        err_desc_string = ', '.join(invalid_fields)
        self.invalid_fields = invalid_fields
        super().__init__(
            self, ('Following fields contain invalid data: {}.'.format(
                err_desc_string)))


def log_exception(fn):
    """Log Exception which occurs.

    The decorator performs logging of Exception that occurred, to log file.
    """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            return result
        except Exception as ex:
            logfile.debug(ex)
            raise
    return wrapper
