from flask import Flask, jsonify
import requests
import os
import json

app = Flask(__name__)

# URL of the dataset
DATA_URL = "http://data.ecan.govt.nz/data/51/Rainfall/Rainfall%20summary%20by%20area/JSON?Sites=SOUTH"
THIS_HOUR_FILE_PATH = "/home/ubuntu/app/this_hour.json"
APPEND_FILE_PATH = "/home/ubuntu/app/append_rainfall.json"
RAINFALL_DATA_FILE_PATH = "/home/ubuntu/app/rainfall_data.json"
RAINFALL_METADATA_FILE_PATH = '/home/ubuntu/app/rainfall_metadata.json'

@app.route('/vajiranath/rainfall/append', methods=['GET'])
def fetch_rainfall_data():
    try:
        # Fetch new data
        response = requests.get(DATA_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        new_data = response.json()
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(THIS_HOUR_FILE_PATH), exist_ok=True)
        
        # Write new data to this_hour.json (overwriting each time)
        with open(THIS_HOUR_FILE_PATH, 'w') as json_file:
            json.dump(new_data, json_file)
        
        # Read existing data from append_rainfall.json if it exists
        existing_data = []
        if os.path.exists(APPEND_FILE_PATH):
            with open(APPEND_FILE_PATH, 'r') as json_file:
                existing_data = json.load(json_file)
        
        # Append new data to existing_data
        if isinstance(existing_data, list):
            existing_data.append(new_data)
        else:
            existing_data = [existing_data, new_data]
        
        # Write the updated data back to append_rainfall.json
        with open(APPEND_FILE_PATH, 'w') as json_file:
            json.dump(existing_data, json_file)
        
        # Return the combined data
        return jsonify(existing_data), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except IOError as e:
        return jsonify({"error": f"File write error: {str(e)}"}), 500
    

@app.route('/vajiranath/rainfall/data', methods=['GET'])
def get_rainfall_data():
    if os.path.exists(APPEND_FILE_PATH):
        with open(APPEND_FILE_PATH, 'r') as file:
            data = json.load(file)
        
        # Save the data to rainfall_data.json
        with open(RAINFALL_DATA_FILE_PATH, 'w') as json_file:
            json.dump(data, json_file)
        
        return jsonify(data)
    else:
        return jsonify({"error": "File not found"}), 404
    
    
@app.route('/vajiranath/rainfall/metadata', methods=['GET'])
def get_rainfall_metadata():
    if os.path.exists(RAINFALL_METADATA_FILE_PATH):
        with open(RAINFALL_METADATA_FILE_PATH, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "File not found"}), 404
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
