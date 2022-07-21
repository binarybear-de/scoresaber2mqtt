#!/usr/bin/env python3
# script to publish user's Scoresaber information to MQTT
# https://github.com/binarybear-de/scoresaber2mqt

import paho.mqtt.client as mqttClient
import time
import configparser
import requests
import sys

# global variable for the state of the connection
isConnected = False

# Source configuration from external config file
config = configparser.ConfigParser()
config.read('/etc/scoresaber.ini')
uid = int(config['scoresaber']['uid'])
mqtt_address = config['mqtt']['address']
port = int(config['mqtt']['port'])
user = config['mqtt']['user']
password = config['mqtt']['password']


def on_connect(client, userdata, flags, rc):
	if rc != 0:
		sys.exit(1)
	global isConnected
	isConnected = True

client = mqttClient.Client("scoresaber2mqtt")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.connect(mqtt_address, port=port)
client.loop_start()

while isConnected != True:  # Wait for connection
	time.sleep(0.1)

data = requests.get('https://scoresaber.com/api/player/76561198078668652/basic')
if data.status_code != 200:
	sys.exit(1)

for item in data.json():
	client.publish(f'games/beatsaber/{item}', data.json()[item])

client.disconnect()
client.loop_stop()
