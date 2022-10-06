#!/usr/bin/python3

import subprocess
import re
import sys
import time

from datetime import datetime

import paho.mqtt.client as mqtt
import ssl

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
client.tls_set(ca_certs="/home/odroid/Lanited_IoT/TLSTools/ca.crt", certfile="/home/odroid/Lanited_IoT/TLSTools/client01.crt",
                    keyfile="/home/odroid/Lanited_IoT/TLSTools/client01.key", cert_reqs=ssl.CERT_NONE,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(True)
print("Connecting...")
client.connect(mqttAddress, mqttPort, 30)

client.loop_start()

#------------------------------------------------------------------------- Sensor Functions
def get_sensor_data():
    command = "sensors | grep 'Package id 0:'"
    sensors_out = subprocess.check_output(["bash", "-c", command])
    #sys.stdout.write( str(sensors_out) )
    return sensors_out.decode('utf-8')

def parse_temps(sensor_data):
    temps = re.findall('\d+(?:\.\d+)?°C ', sensor_data, re.MULTILINE)
    return [x[:-3] for x in temps]

def update_output(temps):
    #sys.stdout.write("Board: %s - Package: %s - Core 0: %s - Core 2: %s\r" %
    #                 (temps[0], temps[1], temps[2], temps[3]))
    #sys.stdout.flush()

    client.publish("/vmhp-dp-01/cpusock-temperature", str(temps[0]), 1, True) #<--------------------------------------------------Sentencias de publicacion
    client.publish("/vmhp-dp-01/cpusock-origin-timestamp", str( datetime.now().isoformat() ), 1, True) #<--------------------------------------------------Sentencias de publicacion

def shutdown():
    client.loop_stop(force=True)
    client.disconnect()
    print()
    print("Goodbye!")
    print()

#-------------------------------------------------------------------------- Main program
print()
print("System temperatures (°C) reported by the 'sensors' command (Ctrl-C to stop):")
try:
    while True:
        #data = get_sensor_data()
        #temp_values = parse_temps(data)
        update_output("0")
        client.loop_stop(force=True)
        client.reconnect()
        client.loop_start()
        time.sleep(0.5)
except KeyboardInterrupt:
    shutdown()
