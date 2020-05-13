import paho.mqtt.client as mqtt
import json

class Krankenhaus:
	def _init_(self, auswahl, verfuegbarkeit): 
		self.auswahl = auswahl
		self.verfuegbarkeit = verfuegbarkeit
		
m_krankenhaus = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([
                    ("krankenhaus/server/order", 2), 
                    ("krankenhaus/server/krankenhaus1", 2),
                    ])

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic.endswith('krankenhaus1')):
        register_company(msg.payload)
    if(msg.topic.endswith('order')):
        process_order(msg.payload)
        
def process_order(data):
    js = json.loads(data)
    name = js['name']
    adresse = js['adresse']
    platz = js['platz']
    narricht = js['narricht']
    
    selected_krankenhaus = None
    
    for krankenhaus in m_krankenhaus
     if adresse in krankenhaus.ort:
        selected_krankenhaus = krankenhaus
	
response = ''
if seleted_krankenhaus != None:
	response = 'The krankenhaus '+selected_krankenhaus.ort+ 'ist kein Platz frei'
	client.publish(selected_krankenhaus.topic, name+ ' wants '+
    
