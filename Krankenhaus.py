import paho.mqtt.client as mqtt
import json

class Krankenhaus:
	def _init_(self, auswahl, verfuegbarkeit): 
		self.auswahl = auswahl
		self.verfuegbarkeit = verfuegbarkeit
		
m_krankenhaus = []

def on_connect(client, userdata, flags, rc):
	client.subscribe(["hshl/krankenhaus/krankenhaus1, 2)])
			  
def on_message(client, userdata, msg):
	print(str(msg.payload))
			
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
			 
client.connect("test.mosquitto.org, 1883, 60)
	       
data = {
    "name": "Krankenhaus 1", 
    "verfuegbarkeit" :["Platz frei", "Kein Platz frei"], 
    "topic": "hshl/krankenhaus/krankenhaus1"
    }
client.publish("hshl/krankenhaus/krankenhaus1", json.dumps(data))

client.loop_forever()
