import paho.mqtt.client as mqtt
import os
from threading import Thread
import time

os.system('cls')
print('-----------------------------------')
print('Welcome to MQTT Chat Bot')
print('-----------------------------------')
name = input('what is your name: ').strip()
username = 'kcqjsmsf'
password = 'z2AmYboRBXTk'
broker_ip = 'm24.cloudmqtt.com'
broker_port_no = 16966
topic = input("Topic: ").strip().lower()
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
    chat_control()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(broker_ip, broker_port_no, 60)


def client_loop():
    client.loop_start()


def chat_control():
    try:
        message = input('Input Message: ').strip()
        if message != '':
            client.publish(topic, name.capitalize()+': '+message)
    except Exception as e:
        print('Error: {}'.format(e))


def main():
    try:
        '''
        h1 = Thread(target=client_loop)
        h1.start()
        time.sleep(2)
        h2 = Thread(target=chat_control)
        h2.start()
        '''
        client_loop()
        chat_control()
    except KeyboardInterrupt:
        print('\nProgramme terminated')


if __name__ == "__main__":
    main()
