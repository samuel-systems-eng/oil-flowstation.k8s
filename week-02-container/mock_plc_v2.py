import time
import random
import json
import paho.mqtt.client as mqtt # New: The MQTT "transmitter" library
import os

# SRE Best Practice: Get broker address from an Environment Variable
# If not set, defaults to 'localhost'
MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto-service")
MQTT_PORT = 1883
MQTT_TOPIC = "flowstation/telemetry"

def generate_flow_data():
    pressure = round(random.uniform(40, 60), 2)
    flow_rate = round(random.uniform(200, 250), 2)
    return {"pressure": pressure, "flow": flow_rate, "status": "OK"}

if __name__ == "__main__":
    client = mqtt.Client()
    
    # Try to connect to "Junction Box"
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print(f"Connected to Broker at {MQTT_BROKER}")
    except Exception as e:
        print(f"Failed to connect: {e}")
        exit(1)

    while True:
        data = generate_flow_data()
        # "Publish" data instead of just printing it
        client.publish(MQTT_TOPIC, json.dumps(data))
        print(f"Published to {MQTT_TOPIC}: {data}")
        time.sleep(5)
