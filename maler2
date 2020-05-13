import paho.mqtt.client as mqtt
import json

class Maler:
    def __init__(self, name, farben_list):
        self.name = name
        self.pizza_list = farben_list

companies = []

def on_connect(client, userdata, flags, rc):
    client.subscribe([                    
                    ("hshl/maler/maler1", 2),
                    ])

def on_message(client, userdata, msg):
    print(str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

data = {
    "name": "Maler 1", 
    "farben_list" :["Blau", "DBlau"], 
    "topic": "hshl/maler/maler1"
    }
client.publish("hshl/server/maler", json.dumps(data))

client.loop_forever()
