from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app, origins=["*"])  

@app.route('/api/listings')
def get_listings():
    with open('listings.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
