import paho.mqtt.client as mqtt
import time
import json
from mysql_ins import mysqlUpdater

broker_address="172.20.240.114"

def on_connect(client, userdata, flags, rc):
    print(rc)
    print("Connection Successful")

def on_subscribe(client, userdata, mid, qos):
    print("subscribed")

def on_message(client, userdata, message):
    print("Message received: Message topic is: " + message.topic)
    message_content=str(message.payload.decode("utf-8", "ignore"))
    print("Message type is: ", type(message_content))
    print("Message contents are: ", message_content)
    conv_data=json.loads(message_content)
    print("The type of converted data is: ", type(conv_data))
    with open("/home/imranq/Desktop/iot_final/received_data.json", "w") as f:
        json.dump(conv_data, f)
    mysqlUpdater()
    
print("creating new instance")
client=mqtt.Client("linux_client")

print("connecting to broker")
client.connect(broker_address)
client.on_connect=on_connect
client.on_subscribe=on_subscribe
client.on_message=on_message

#client.loop_forever()

client.loop_start()
client.subscribe("sensor/json")
time.sleep(700)
client.loop_stop()

