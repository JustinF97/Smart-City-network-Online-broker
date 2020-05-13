import paho.mqtt.client as mqtt
import json

ask = True

def on_connect(client, userdata, flags, rc):
    client.subscribe([
                    ("hshl/customer/myid", 2), 
                    ])

def on_message(client, userdata, msg):
    global ask 
    ask = True
    print(str(msg.payload))
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_start()


def request_farbe(farbe, quantity):
    data = {
        "name": "Charles",
        "farbe": farbe,
        "quantity": quantity,
        "topic": "hshl/customer/myid",
    }
    client.publish("hshl/server/order", json.dumps(data))
    
    while True:
    if ask:
        farbe = input("Enter a Farbe name: ")
        quantity = input("Welche Farbe "+farbe+" boentigst du? ")
        request_farbe(farbe, quantity)
        ask = False

