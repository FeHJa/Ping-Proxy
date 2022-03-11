#!/usr/bin/env python
import time
import os
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

### Definition
mqtt_broker = "10.1.0.10"
mqtt_port = 1883
hostnames = {"ping1":"10.15.5.1", "ping2":"10.15.5.96", "ping3":"10.6.0.20"}
repeat_time = 30
mqtt_topic = "hal/ping/"

### MQTT Connection
client = mqtt.Client()
client.on_connect = on_connect
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

### Endless Loop
while True:
	time.sleep(repeat_time)
	for name,hostname in hostnames.items():
		response = os.system("ping -c 1 -w2 " + hostname + " > /dev/null 2>&1")
		if response == 0:
			status = 'Connected'
		else:
			status = 'Disconnected'
		client.publish(mqtt_topic + name, status)