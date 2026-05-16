from iot_layer.mqtt.mqtt_client import MicrogridMQTTClient
from iot_layer.config_iot import TOPIC_CONTROL
from utils.logger import logger

class ControlService:
    def __init__(self):
        # ActuatorController-ku bathila MQTT Client-a use panrom
        self.mqtt_client = MicrogridMQTTClient(client_id="API_Control_Service")

    def send_command(self, device_id: str, action: str):
        """
        IoT Layer-oda MQTT topic-ku direct-ah control signal-a anupum.
        Example: microgrid/control/Battery_Unit -> {"action": "DISCHARGE"}
        """
        try:
            self.mqtt_client.connect()
            payload = {
                "device_id": device_id,
                "action": action,
                "command_type": "REMOTE_OVERRIDE"
            }
            
            # Specific device topic-ku publish panrom
            topic = f"{TOPIC_CONTROL}/{device_id}"
            self.mqtt_client.publish(topic, payload)
            
            logger.info(f"Control command sent via MQTT: {action} to {device_id}")
            return {"success": True, "msg": f"Command {action} published to {topic}"}
            
        except Exception as e:
            logger.error(f"Failed to send control command: {e}")
            return {"success": False, "msg": str(e)}