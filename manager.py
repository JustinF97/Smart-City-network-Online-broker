import paho.mqtt.client as mqtt
import json

class Company:
    def __init__(self, name, gps_list, topic):
        self.name = name
        self.gps_list = gps_list
        self.topic = topic
 
companies = []

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe([
                  ("hshl/server/order", 2),
                  ("hshl/server/company", 2),
                  ])
  
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic.endswith('company')):
        register_company(msg.payload)
    if(msg.topic.endswith('order')):
        process_order(msg.payload)

def process_order(data):
    js = json.loads(data)
    name = js['name']
    pizza = js['adresse']
    notfall = js['notfall']
    topic = js['topic']
  
    selected_company = None

    for company in companies:
        if pizza in company.gps_list:
            selected_company = company
           
    response = ''
    if selected_company != None:
        response = 'The company '+selected_company.name+ ' hat noch einen Platz frei'
        client.publish(selected_company.topic, name+ ' wants '+notfall+ ' Paltz '+gps)
    else:
        response = 'Sorry, keiner hat einen Platz'
    
    client.publish(topic, response)
    
    
    
    
