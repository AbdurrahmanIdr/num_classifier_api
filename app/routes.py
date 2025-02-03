"""
This module contains the route definitions for the Flask application.
"""

from flask import Blueprint, request
from app.controllers import classify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/classify-number', methods=['GET'])
def classify_number():
    """
    Endpoint to classify a number.

    This route handles GET requests to the '/api/classify-number' URL.
    It expects a query parameter 'number' and uses the classify function
    from the app.controllers module to classify the number.

    Returns:
        Response: The result of the classify function.
    """
    number = request.args.get('number')
    return classify(number)
