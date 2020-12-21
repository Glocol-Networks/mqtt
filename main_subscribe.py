import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("gpsd_ws/gps","gpsd_ws/extended","gpsd_ws/data")  # Subscribe to the topics , receive any messages published on them


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    with open('./test.txt','a+') as f:
        f.write("Message received: "  + msg.payload + "\n")

client = mqtt.Client()
client.connect('127.0.0.1', 1883, 60)
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message

client.loop_forever()  # Start networking daemon