"""Custom Exceptions module."""

import functools

import logging
logfile = logging.getLogger(__name__)


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

