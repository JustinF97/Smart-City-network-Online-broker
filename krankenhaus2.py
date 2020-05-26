import paho.mqtt.client as mqtt
import json

class Krankenhaus:
  def _init_(self, name, gps):
    self.name = name
    self.gps = gps
   
mKrankenhaus = []

def on_connect(client, userdata, flags, rc):
  client.subscribe([("hshl/krankenhaus/krankenhaus2", 2),])

def on_message(client, userdata, msg):
  print(str(msg.payload))
  
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitoo.org", 1883, 60)

data = {
  "name": Katholisches Krankenhaus Lippstadt
  "gps": Klosterstraße 31
  "topic": "hshl/krankenhaus/krankenhaus2"
   }
client.publish("hshl/server/krankenhaus",json.dumps(data))

client.loop_forever()
