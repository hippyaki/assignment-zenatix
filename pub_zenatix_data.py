import paho.mqtt.client as mqtt
import time, random , json
import smbus2, bme280 #Comment to use simulated data

# BME280 sensor Initialization (comment below 3 lines to use simulated data)
address = 0x77
bus = smbus2.SMBus(1) 
calibration_params = bme280.load_calibration_params(bus, address)

# MQTT Broker & the topic to use 
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "zenatixiot/akshayan/temperature"

#Return the connection status
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

def zenatix_temp_pub():
    
    # Connect to MQTT broker using Paho
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2) 
    client.on_connect = on_connect
    client.connect(BROKER_ADDRESS, BROKER_PORT)

    while True:
        
        #Uncomment below line to to use simulated data
        #temp = round(random.uniform(20, 31), 2) 

        #Comment below 2 lines if using simulated data
        data = bme280.sample(bus, address, calibration_params)
        temp = round(data.temperature, 2)
        
        #Update current time - from epoch seconds to IST
        timestamp = int(time.time())
        ist_offset = 5.5 * 3600
        ist_time = time.localtime(timestamp + ist_offset)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', ist_time)

        #Prepare JSON object with time and data
        sensor_data = {
            "sensorData": [
                {
                    "timestamp": formatted_time,
                    "temperature": temp
                }
            ]
        }
        
        # Serialize object to JSON format
        message = json.dumps(sensor_data)

        # Publish the JSON to MQTT topic
        client.publish(TOPIC, message)
        print(f"Published: {message}")
        
        # Wait for 60 seconds before next reading
        time.sleep(60)

if __name__ == "__main__":
    zenatix_temp_pub()
