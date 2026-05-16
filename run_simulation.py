import time
from iot_layer.sensor_data_simulator import SensorSimulator
from core_layer.digital_twin.twin_state import DigitalTwinState
from utils.logger import logger

def start_simulation():
    simulator = SensorSimulator()
    twin = DigitalTwinState()
    
    logger.info("Microgrid Simulation Engine Started...")
    
    try:
        while True:
            # 1. Get current simulated metrics
            current_metrics = twin.get_current_state()
            
            # 2. Stream to IoT Layer (MQTT)
            simulator.start_streaming(current_metrics)
            
            # 3. Wait for next time step (e.g., 2 seconds)
            time.sleep(2)
            
    except KeyboardInterrupt:
        logger.info("Simulation Stopped by User.")

if __name__ == "__main__":
    start_simulation()