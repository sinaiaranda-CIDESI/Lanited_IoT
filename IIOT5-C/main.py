#!/usr/bin/python3

import subprocess
import re
import sys
import time

import paho.mqtt.client as mqtt
import ssl

#------------------------------------------------------------------------

from itsybitsy_module.read_serial import*
from schneider_module.medidor_de_energia_v3 import*

with open('IIOT5-C/topics.txt') as f:
    topics = f.readlines()

for topic in topics:
    print(topic)
    
#------------------------------------------------------------------------Environment Vars
mqttAddress = "inginx.icidesi.mx" #<----------- Si no resuelve direccion ip es 10.40.30.32
mqttPort = 8883
mqttClientID = "IIOT-A"
mqttUserName = "user02"
mqttPassword = "C1d3siMQTTUser20220322"

#----------------------------------------------------------------------- MQTT Functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    #client.subscribe("test")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")
        shutdown()

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

#------------------------------------------------------------------------------------------------------------------------
client = mqtt.Client(client_id=mqttClientID, clean_session=True, userdata=None, protocol=mqtt.MQTTv311, transport="tcp")
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.username_pw_set(username=mqttUserName, password=mqttPassword)
client.tls_set(ca_certs="/home/odroid/IIOT5-C/TLSTools/ca.crt", certfile="/home/odroid/IIOT5-C/TLSTools/client01.crt",
                    keyfile="/home/odroid/IIOT5-C/TLSTools/client01.key", cert_reqs=ssl.CERT_NONE,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(True)
print("Connecting...")
client.connect(mqttAddress, mqttPort, 30)

client.loop_start()

def shutdown():
    client.loop_stop(force=True)
    client.disconnect()
    print()
    print("Goodbye!")
    print()

#-------------------------------------------------------------------------- Main program
print()

try:
    while True:
        data_set_1 = read_data()
        data_set_2 = read_energy_monitor()
        
        client.publish(topics[0], str(data_set_1['TEMPERATURE']['VALUE']), 1, True)
        client.publish(topics[1], str(data_set_1['TEMPERATURE']['TIMESTAMP']), 1, True)
        client.publish(topics[2], str(data_set_1['HUMIDITY']['VALUE']), 1, True)
        client.publish(topics[3], str(data_set_1['HUMIDITY']['TIMESTAMP']), 1, True)
        
        client.publish(topics[4], str(data_set_2['CURRENT_PH1']['VALUE']), 1, True)
        client.publish(topics[5], str(data_set_2['CURRENT_PH1']['TIMESTAMP']), 1, True)
        client.publish(topics[6], str(data_set_2['CURRENT_PH2']['VALUE']), 1, True)
        client.publish(topics[7], str(data_set_2['CURRENT_PH2']['TIMESTAMP']), 1, True)
        client.publish(topics[8], str(data_set_2['CURRENT_PH3']['VALUE']), 1, True)
        client.publish(topics[9], str(data_set_2['CURRENT_PH3']['TIMESTAMP']), 1, True)
        client.publish(topics[10], str(data_set_2['CURRENT_AVG']['VALUE']), 1, True)
        client.publish(topics[11], str(data_set_2['CURRENT_AVG']['TIMESTAMP']), 1, True)
        client.publish(topics[12], str(data_set_2['VOLTAGE_L1_L2']['VALUE']), 1, True)
        client.publish(topics[13], str(data_set_2['VOLTAGE_L1_L2']['TIMESTAMP']), 1, True)
        client.publish(topics[14], str(data_set_2['VOLTAGE_L2_L3']['VALUE']), 1, True)
        client.publish(topics[15], str(data_set_2['VOLTAGE_L2_L3']['TIMESTAMP']), 1, True)
        client.publish(topics[16], str(data_set_2['VOLTAGE_L3_L1']['VALUE']), 1, True)
        client.publish(topics[17], str(data_set_2['VOLTAGE_L3_L1']['TIMESTAMP']), 1, True)
        client.publish(topics[18], str(data_set_2['ACTIVE_POWER_L1']['VALUE']), 1, True)
        client.publish(topics[19], str(data_set_2['ACTIVE_POWER_L1']['TIMESTAMP']), 1, True)
        client.publish(topics[20], str(data_set_2['ACTIVE_POWER_L2']['VALUE']), 1, True)
        client.publish(topics[21], str(data_set_2['ACTIVE_POWER_L2']['TIMESTAMP']), 1, True)
        client.publish(topics[22], str(data_set_2['ACTIVE_POWER_L3']['VALUE']), 1, True)
        client.publish(topics[23], str(data_set_2['ACTIVE_POWER_L3']['TIMESTAMP']), 1, True)
        client.publish(topics[24], str(data_set_2['TOTAL_ACTIVE_POWER']['VALUE']), 1, True)
        client.publish(topics[25], str(data_set_2['TOTAL_ACTIVE_POWER']['TIMESTAMP']), 1, True)
        client.publish(topics[26], str(data_set_2['TOTAL_REACTIVE_POWER']['VALUE']), 1, True)
        client.publish(topics[27], str(data_set_2['TOTAL_REACTIVE_POWER']['TIMESTAMP']), 1, True)
        client.publish(topics[28], str(data_set_2['TOTAL_APPARENT_POWER']['VALUE']), 1, True)
        client.publish(topics[29], str(data_set_2['TOTAL_APPARENT_POWER']['TIMESTAMP']), 1, True)
        client.publish(topics[30], str(data_set_2['POWER_FACTOR']['VALUE']), 1, True)
        client.publish(topics[31], str(data_set_2['POWER_FACTOR']['TIMESTAMP']), 1, True)
        client.publish(topics[32], str(data_set_2['FREQUENCY']['VALUE']), 1, True)
        client.publish(topics[33], str(data_set_2['FREQUENCY']['TIMESTAMP']), 1, True)
        
        client.loop_stop(force=True)
        client.reconnect()
        client.loop_start()
        time.sleep(0.5)
except KeyboardInterrupt:
    shutdown()
