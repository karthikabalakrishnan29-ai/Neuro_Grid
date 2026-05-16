import time
import random
from iot_layer.mqtt.mqtt_client import MicrogridMQTTClient
from iot_layer.config_iot import TOPIC_TELEMETRY

class SensorSimulator:
    def __init__(self):
        self.client = MicrogridMQTTClient()
        
    def generate_packet(self, device_id, value, unit):
        return {
            "device_id": device_id,
            "value": round(value, 4),
            "unit": unit,
            "timestamp": time.time()
        }

    def start_streaming(self, asset_data):
        """Asset data-va stream pannum"""
        self.client.connect()
        for device, val in asset_data.items():
            packet = self.generate_packet(device, val, "kW")
            self.client.publish(f"{TOPIC_TELEMETRY}/{device}", packet)