#sends the json to the mosquitto

import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    print(rc)
    print("Connection Successful")
    
def on_publish(client, userdata, result):
    print(result)
    print("Publish Successful")

def sendToMqtt():
    broker_address="172.20.240.114"
    topic="sensor/json"
    with open('/home/pi/sensor_data/data.json', 'r') as f:
        py_obj = json.load(f)
    json_out=json.dumps(py_obj)
    print("creating new instance")
    client = mqtt.Client("pi_client")
    print("connecting to broker")
    client.connect(broker_address)
    client.on_connect=on_connect
    client.on_publish=on_publish
    client.loop_start()
    client.publish("sensor/json", json_out)
    time.sleep(60)
    client.loop_stop()
    client.disconnect()

