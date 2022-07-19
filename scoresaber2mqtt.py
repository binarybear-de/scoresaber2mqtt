#!/usr/bin/env python3
# script to publish user's Scoresaber information to MQTT
# https://github.com/binarybear-de/scoresaber2mqt

import paho.mqtt.client as mqttClient
import time
import configparser
import requests
import sys

isConnected = False  # global variable for the state of the connection

# Source configuration from external config file
config = configparser.ConfigParser()
config.read('scoresaber.ini')
uid = int(config['scoresaber']['uid'])

broker_address = config['mqtt']['address']
port = int(config['mqtt']['port'])
user = config['mqtt']['user']
password = config['mqtt']['password']

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global isConnected  # Use global variable
        isConnected = True  # Signal connection
    else:
        sys.exit(1)

client = mqttClient.Client("Python")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=port)  # connect to broker
client.loop_start()  # start the loop

while isConnected != True:  # Wait for connection
    time.sleep(1)

try:
    data = requests.get('https://scoresaber.com/api/player/<player_id>/basic')
    if data.status_code == 200:
         for item in data.json():
              client.publish(f'games/beatsaber/{item}', data.json()[item])

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
