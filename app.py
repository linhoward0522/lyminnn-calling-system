from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_range = {"start": 0, "end": 0}

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify(current_range)

@app.route('/update', methods=['POST'])
def update_status():
    data = request.get_json()
    current_range["start"] = int(data.get("start", 0))
    current_range["end"] = int(data.get("end", 0))
    return jsonify({"success": True, "current_range": current_range})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
