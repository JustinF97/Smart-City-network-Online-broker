import paho.mqtt.client as mqtt
import json

class Company:
    def __init__(self, name, pizza_list, topic):
        self.name = name
        self.pizza_list = pizza_list
        self.topic = topic

companies = []
