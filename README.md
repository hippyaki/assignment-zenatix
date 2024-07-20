# Zenatix IoT Assignment Submission

## Overview

This project involves setting up a Raspberry Pi running Ubuntu Server 20.04 with a BME280 sensor to publish data to an MQTT broker (HiveMQ). Another machine will subscribe to this topic, store the data in a JSON file (`sensor_data.json`), and host a server using Python Flask to provide access to the latest data via a GET request endpoint.

## Goals

1. **Publish Sensor Data**: The Raspberry Pi, equipped with a BME280 sensor, will publish data to an MQTT broker.
2. **Subscribe and Store Data**: Another machine will subscribe to the MQTT topic and store the received data in a JSON file.
3. **Host a Flask Server**: The subscriber machine will host a Flask server with a `/temperature` endpoint to retrieve the latest sensor data.

## Demonstration Video

Watch the demonstration video showing the threshold-based alarm trigger on YouTube: [![Assignment Demo Video - Zenatix IoT](https://img.youtube.com/vi/hd3X1OxrZwY/0.jpg)](https://www.youtube.com/watch?v=hd3X1OxrZwY)

 [Assignment Demo Video - Zenatix IoT](https://youtu.be/hd3X1OxrZwY)


## Repository Structure

```
.
├── pub_zenatix_data.py
├── sub_zenatix_data.py
├── HTTP_server.py
├── sensor_data.json
├── requirements.txt
└── README.md
```

## Requirements

Ensure you have Python 3.6+ installed on both the Raspberry Pi and the subscriber machine. Use the `requirements.txt` file to install necessary dependencies.

## Setup Instructions

### Step 1: Set Up the Python Environment

1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/hippyaki/assignment-zenatix.git
   cd assignment-zenatix
   ```

2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

### Step 2: Raspberry Pi Configuration

1. **Connect the BME280 sensor** to the Raspberry Pi.
2. **Run the publisher script** on the Raspberry Pi:
   ```sh
   python pub_zenatix_data.py
   ```

### Step 3: Subscriber Machine Configuration

1. **Run the subscriber script** on the other machine to subscribe to the MQTT topic and store data locally:
   ```sh
   python sub_zenatix_data.py
   ```

2. **Run the Flask server** to provide access to the latest sensor data:
   ```sh
   python HTTP_server.py
   ```

## Program Descriptions

### pub_zenatix_data.py

This script runs on the Raspberry Pi and publishes sensor data from the BME280 to an MQTT broker. Ensure that the required modules specified in the `requirements.txt` file are installed before running this script.

### sub_zenatix_data.py

This script runs on another machine (preferably Linux) and subscribes to the MQTT topic. It stores the received data in a JSON file named `sensor_data.json` locally.

### HTTP_server.py

This script uses Flask to host a server on the subscriber machine. It provides a `/temperature` endpoint that responds with the latest data in the `sensor_data.json` file.

## Usage

1. **Start the publisher** on the Raspberry Pi:
   ```sh
   python pub_zenatix_data.py
   ```

2. **Start the subscriber** on the other machine:
   ```sh
   python sub_zenatix_data.py
   ```

3. **Start the Flask server** on the subscriber machine:
   ```sh
   python HTTP_server.py
   ```

4. **Access the data** by sending a GET request to the `/temperature` endpoint:
   ```sh
   curl http://localhost:5000/temperature
   ```

This request will return the latest temperature data stored in the `sensor_data.json` file.

## Conclusion

Follow these steps to set up the environment, run the scripts, and access the sensor data. Ensure all dependencies are installed as per the `requirements.txt` file. This setup enables you to collect, store, and retrieve sensor data efficiently. Looking forward to work at Zenatix Solutions.

For any issues or queries, feel free to contact me at [akshayan.sinha@gmail.com].
