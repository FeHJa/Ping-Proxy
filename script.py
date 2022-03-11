#!/usr/bin/env python
import time
import os
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.connect("10.1.0.10", 1883, 60)
client.loop_start()

hostname1 = "10.15.5.1"
hostname2 = "10.15.5.96"
hostname3 = "10.6.0.20"

while True:
	time.sleep(30)
	response1 = os.system("ping -c 1 -w2 " + hostname1 + " > /dev/null 2>&1")
	response2 = os.system("ping -c 1 -w2 " + hostname2 + " > /dev/null 2>&1")
	response3 = os.system("ping -c 1 -w2 " + hostname3 + " > /dev/null 2>&1")
	if response1 == 0:
		status1 = 'Connected'
	else:
		status1 = 'Disconnected'
	if response2 == 0:
		status2 = 'Connected'
	else:
		status2 = 'Disconnected'
	if response3 == 0:
		status3 = 'Connected'
	else:
		status3 = 'Disconnected'
	client.publish("hal/ping/ping1", status1)
	client.publish("hal/ping/ping2", status2)
	client.publish("hal/ping/ping3", status3)