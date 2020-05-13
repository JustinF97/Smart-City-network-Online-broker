import paho.mqtt.client as mqtt
import json

class Maler:
    def __init__(self, name, maler_list, topic):
        self.name = name
        self.maler_list = maler_list
        self.topic = topic

companies = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([
                    ("hshl/server/order", 2), 
                    ("hshl/server/maler", 2),
                    ])
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic.endswith('maler')):
        register_maler(msg.payload)
    if(msg.topic.endswith('order')):
        process_order(msg.payload)
        
def process_order(data):
    js = json.loads(data)
    name = js['name']
    farbe = js['farbe']
    topic = js['topic']
    
    selected_maler = None

    for maler in companies:
        if farbe in maler.farbe_list:
            selected_maler = maler
            
    response = ''
    if selected_maler != None:
        response = 'Der Maler '+selected_maler.name+ ' hat deine Farbe vorhanden'
        client.publish(selected_maler.topic, name+ ' wants '+farbe+ ' farbe '+farbe)
    else:
        response = 'Sorry, nobody has this kind of Farbe'
    
    client.publish(topic, response)

def register_maler(data):
    js = json.loads(data)
    maler = maler(js['name'], js['maler_list'], js['topic'])
    companies.append(maler)
    print('#####################')
    for c in maler:
        print(c.name)
        print(c.maler_list)
        print('--------------')
    print('#####################')
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
