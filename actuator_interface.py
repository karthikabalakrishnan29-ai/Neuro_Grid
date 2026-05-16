from utils.logger import logger
from iot_layer.mqtt.mqtt_client import MicrogridMQTTClient

class ActuatorInterface:
    def __init__(self):
        self.mqtt = MicrogridMQTTClient(client_id="Control_Actuator_IF")
        self.mqtt.connect()

    def send_signal(self, device_id, command):
        """
        Physical hardware-ku command-a forward pannum.
        command: "OPEN", "CLOSE", "START", "STOP"
        """
        topic = f"microgrid/hardware/{device_id}"
        payload = {"device": device_id, "action": command}
        self.mqtt.publish(topic, payload)
        logger.info(f"Signal sent to {device_id}: {command}")
        return True