import paho.mqtt.client as mqtt
import json

# MQTT Broker & the topic to use 
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "zenatixiot/akshayan/temperature"

# Threshold and time window
THRESHOLD = 30.5

# Flag variable to check threshold
danger = 0
flag = False

#Return the connection status and subscribe to topic
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    try:

        # Deserialize JSON format to object
        payload = json.loads(msg.payload.decode())
        sensor_data = payload.get("sensorData", [])

        # Extract temperature data and timestamp from object        
        for data in sensor_data:
            temperature = data.get("temperature")
            timestamp = data.get("timestamp")
            
            if temperature is not None and timestamp is not None:
                
                # Write data to JSON file in received format
                with open('sensor_data.json', 'a') as f:
                    json.dump(data, f)
                    f.write('\n')
                
                
                print(f"Received: {temperature}°C at {timestamp}")

                # Check for Alarm condition
                check_alarm(temperature)

            else:
                print("Invalid data format received")

    except json.JSONDecodeError:
        print("Invalid JSON received")

def check_alarm(data):

    global danger

    # Check if threshold crossed
    if (data > THRESHOLD):
        danger += 1
        if (danger >= 5):
            print("ALARM: Temperature Exceeded! Please check device!!")

    # Race down threshold danger to 0
    else:
        danger=0

def subscribe():

    # Connect to MQTT broker using Paho
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    subscribe()