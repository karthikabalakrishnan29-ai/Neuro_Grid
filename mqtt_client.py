import paho.mqtt.client as mqtt
import json
from iot_layer.config_iot import MQTT_BROKER, MQTT_PORT

class MicrogridMQTTClient:
    def __init__(self, client_id="MG_Gateway"):
        self.client = mqtt.Client(client_id)

    def connect(self):
        self.client.connect(MQTT_BROKER, MQTT_PORT)
        self.client.loop_start()

    def publish(self, topic, payload):
        self.client.publish(topic, json.dumps(payload), qos=1)

    def subscribe(self, topic, callback):
        self.client.on_message = callback
        self.client.subscribe(topic)