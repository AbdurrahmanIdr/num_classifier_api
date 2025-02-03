from flask import Blueprint, request, jsonify
from app.controllers import classify


main_bp = Blueprint('main', __name__)

@main_bp.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    return classify(number)
