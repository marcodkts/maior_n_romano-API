from crypt import methods
from flask import request, jsonify, Blueprint
from controller.major_roman_number import majorRomanNumber

searchBluePrint = Blueprint('searchBluePrint', __name__)

@searchBluePrint.route('/search', methods= ["POST"])
def searchViewer():
    content = request.get_json()["text"]
    response = majorRomanNumber(content)
    return jsonify(response)
