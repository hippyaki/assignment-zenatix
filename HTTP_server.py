from flask import Flask, jsonify
import json

app = Flask(__name__)

def get_last_sensor_value():
    try:
        # Extract latest data in the JSON file
        with open('sensor_data.json', 'r') as f:
            # Loop until reach last line in file
            for line in f:
                pass
            # Store value of last line in variable and return object
            last_line = line
        return json.loads(last_line)
    except:
        return None

# GET request Endpoint - /temperature
@app.route('/temperature', methods=['GET'])
def get_temperature():
    #Receive latest data from local JSON file
    sensor_data = get_last_sensor_value()
    
    # If data exists, send a JSON response body
    if sensor_data:
        return jsonify({"sensorData": [sensor_data]})
    else:
        return jsonify({"error": "No sensor data available"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)