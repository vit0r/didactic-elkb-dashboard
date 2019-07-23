from os import environ
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data/', methods=['POST'])
def data():
    request_data = request.get_json()
    status_code = 200 if request_data else 204
    response = jsonify(status_code, data=request_data)
    return response