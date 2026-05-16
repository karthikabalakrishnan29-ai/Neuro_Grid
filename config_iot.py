# IoT Configuration Settings
MQTT_BROKER = "localhost" # "broker.hivemq.com" for cloud testing
MQTT_PORT = 1883
KEEP_ALIVE = 60

# Topics
TOPIC_TELEMETRY = "microgrid/telemetry"
TOPIC_CONTROL = "microgrid/control"
TOPIC_ALERTS = "microgrid/alerts"

# Simulation Settings
SAMPLING_RATE = 1.0  # Seconds