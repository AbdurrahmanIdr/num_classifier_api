from flask import jsonify
from app.services import get_number_properties
from app.utils import fetch_fun_fact


def classify(number):
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
