import paho.mqtt.client as mqtt
import json

class Krankenhaus:
  def _init_(self, name, gps):
    self.name = name
    self.gps = gps
   
mKrankenhaus = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([
                    ("hshl/server/order", 2), 
                    ("hshl/server/krankenhaus", 2),
                    ])
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic.endswith('krankenhaus')):
        register_maler(msg.payload)
    if(msg.topic.endswith('order')):
        process_order(msg.payload)
        
def process_order(data):
    js = json.loads(data)
    name = js['name']
    gps = js['gps']
    notfall = js['notfall']
    
    selected_krankenhaus = None

    for krankenhaus in mkrankenhaus:
        if gps in krankenhaus.gps:
            selected_krankenhaus = krankenhaus
            
    response = ''
    if selected_krankenhaus != None:
        response = 'Das Krankenhaus '+selected_krankenhaus.name+ ' hat einen Platz frei'
        client.publish(selected_krankenhaus.gps, name+ ' benötigt einen Platz ')
    else:
        response = 'Leider haben wir'+gps+'keinen platz'
    
    client.publish(gps, response)

def register_krankenhaus(data):
    js = json.loads(data)
    maler = maler(js['name'], js['gps'])
    companies.append(krankenhaus)
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
