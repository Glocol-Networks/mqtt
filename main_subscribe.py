import paho.mqtt.client as mqtt
import csv
from csv import writer,reader
import os
import pandas as pd


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("gpsd_ws/gps","gpsd_ws/extended","gpsd_ws/data")  # Subscribe to the topics , receive any messages published on them


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    with open('./test.json','a+') as f:
        f.write("Message received: "  + msg.payload + "\n")
    df = pd.read_json (r'./test.json')
    df.to_csv (r'./output.csv', mode='a', index = None)
    if os.path.exists('./test.json'):
        os.remove('./test.json')

broker_address= "192.168.0.6"  #Broker address
port = 1883                         #Broker port
user = "me"                    #Connection username
password = "abcdef"            #Connection password

client = mqtt.Client("Python")
client.username_pw_set(user, password=password)
client.connect(broker_address, port, 60)
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message

client.loop_forever()  # Start networking daemon