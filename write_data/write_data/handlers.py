"""Application Handlers.

Requests are redirected to handlers, which are responsible for getting
information from the URL and passing it down to the logic layer.
"""

from flask import jsonify
from flask import request
from werkzeug.exceptions import HTTPException

from write_data import app
from write_data import config
from write_data.logic import write_data


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


@app.route('/xml_result', methods=['PUT'])
def post_vendor_template():
    """Write XML to file.

    Returns:
        flask.Response: Response with success/error result.
    """
    data = request.get_json()
    xml_str_to_write = data.get('xml')
    result = write_data.write_xml_to_file(xml_str_to_write)
    return jsonify({'xml': result})
