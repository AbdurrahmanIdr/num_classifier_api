"""
This module contains the controller functions for the Flask application.

It includes functions to classify numbers and return their properties along with a fun fact.
"""

from flask import jsonify
from app.services import get_number_properties
from app.utils import fetch_fun_fact

def classify(number):
    """
    Classify a given number and return its properties and a fun fact.

    This function takes a number as input, determines its properties
    (such as whether it is prime or perfect), calculates the digit sum,
    and fetches a fun fact about the number. The results are returned
    as a JSON response.

    Args:
        number (str): The number to classify.

    Returns:
        Response: A Flask JSON response containing the number's properties
                  and a fun fact, or an error message if the input is invalid.
    """
    try:
        number = int(number)

        properties = get_number_properties(number)
        fun_fact = fetch_fun_fact(number)

        return jsonify({
            "number": number,
            "is_prime": properties["is_prime"],
            "is_perfect": properties["is_perfect"],
            "properties": properties["properties"],
            "digit_sum": properties["digit_sum"],
            "fun_fact": fun_fact
        })
    except ValueError:
        return jsonify({"number": number, "error": True}), 400
