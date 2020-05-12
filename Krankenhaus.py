import paho.mqtt.client as mqtt
import json

class Krankenhaus:
	def _init_(self, auswahl, verfuegbarkeit): 
		self.auswahl = auswahl
		self.verfuegbarkeit = verfuegbarkeit
		
m_krankenhaus = []
