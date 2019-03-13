import paho.mqtt.client as mqtt
import os
from threading import Thread
import time

os.system('clear')
print('-----------------------------------')
print('Welcome to MQTT Chat Bot')
print('-----------------------------------')
name = input('what is your name: ').strip()
username = input('Username of Broker: ').strip()
password = input('Password of Broker: ').strip()
broker_ip = input("Broker's IP: ").strip()
broker_port_no = int(input("Broker's Port no: ").strip())
topic = input("Topic: ").strip()
print('-----------------------------------')


# Callback Function on Connection with MQTT Server
def on_connect(connect_client, userdata, flags, rc):
    print("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    connect_client.subscribe(topic)


# Callback Function on Receiving the Subscribed Topic/Message
def on_message(message_client, userdata, msg):
    # print the message received from the subscribed topic
    print(str(msg.payload, 'utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)


def client_loop():
    client.loop_forever()


def chat_control():
    while True:
        try:
            message = input('Input Message: ').strip().lower()
            client.publish(topic, name.capitalize()+': '+message)
        except Exception as e:
            print('Error: {}'.format(e))


def main():
    try:
        h1 = Thread(target=client_loop)
        h1.start()
        time.sleep(2)
        h2 = Thread(target=chat_control)
        h2.start()
    except KeyboardInterrupt:
        print('\nProgramme terminated')
