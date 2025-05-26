from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route('/api/listings')
def get_listings():
    with open('listings.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
