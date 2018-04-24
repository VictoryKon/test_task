"""Application Handlers.

Requests are redirected to handlers, which are responsible for getting
information from the URL and passing it down to the logic layer.
"""

from flask import jsonify
from flask import request
from fetch_data import app
from fetch_data import config
from fetch_data.logic import fetch_data as fetch_data_logic


from werkzeug.exceptions import HTTPException


@app.errorhandler(Exception)
def handle_error(e):
    """Handle the errors returned by handlers."""
    error_code = config.INTERNAL_SERVER_ERROR_CODE
    if isinstance(e, HTTPException):
        error_code = e.code
    error = 'During fetching XML data following error occurred: {}'.format(
                    str(e))
    return jsonify(error=error), error_code


@app.route(config.HEALTH_CHECK, methods=['GET'])
def health():
    """Check the health of the application."""
    return jsonify({'status': 'ok'})


@app.route('/initial_data', methods=['GET'])
def countries_get():
    """Get XML data from files.

    Returns:
        flask.Response: JSON object containing XML read from files.
    """
    filenames = request.args.getlist('filename')
    result = fetch_data_logic.process_files(filenames)
    return jsonify({'xml': result})
