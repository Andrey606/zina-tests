import paho.mqtt.client as mqtt
import time
import json

class MQTT():
    client = mqtt.Client("P1")

    def __init__(self, ip='192.168.50.168', port=8883, username="raspberrypi", password="omo",
                 topicTX="hubCommands/", topicRX="hubEvents/"):
        self.receved_message = ""
        self.status = False
        self.IP = ip
        self.port = port
        self.USERNAME = username
        self.PASS = password
        self.topicTX = topicTX + username
        self.topicRX = topicRX + username

    def create_connection(self):
        self.client.on_message = self.on_message  # attach function to callback
        self.client.username_pw_set(self.USERNAME, self.PASS)
        self.client.connect(self.IP, self.port, 60)  # connect to broker
        self.client.loop_start()  # start the loop
        self.client.subscribe(self.topicRX, 2)

    def send(self, message):
        self.receved_message = None
        self.status = False
        self.client.publish(self.topicTX, message)
        t = time.time()
        while True:
            if (time.time() - t) > 5:
                print("TIMEOUT")
                break;
            if self.status:
                break;
        return self.receved_message

    def close_connection(self):
        self.client.loop_stop()

    def on_message(self, client, userdata, message):
        answer = str(message.payload.decode("utf-8"))
        # print("message received " ,str(message.payload.decode("utf-8")))
        # print("message topic=",message.topic)
        # print("message qos=",message.qos)
        # print("message retain flag=",message.retain)
        self.status = True
        self.receved_message = answer


def send(command):
    client = MQTT()
    client.create_connection()
    event = client.send(json.dumps(command))
    client.close_connection()

    return json.loads(event)
