from flask import Flask, jsonify
from utils import check_and_update_data, load_existing_data, load_metadata, scheduled_task

app = Flask(__name__)

@app.route('/vsu37/rainfall_data', methods=['GET'])
def get_rainfall_data():
    data = load_existing_data()
    return jsonify(data)

@app.route('/vsu37/update_data', methods=['GET'])
def update_data():
    check_and_update_data()
    return jsonify({"message": "Data updated successfully"}), 200


@app.route('/vsu37/rainfall_metadata', methods=['GET'])
def get_rainfall_metadata():
    data = load_metadata()
    return jsonify(data)

if __name__ == '__main__':
    # For debugging: Run the update function once at startup
    check_and_update_data()
    
    app.run(host='0.0.0.0', port=5000)
