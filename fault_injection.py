import random

class FaultInjector:
    def __init__(self):
        self.fault_types = ["SHORT_CIRCUIT", "VOLTAGE_SAG", "SENSOR_BIAS"]

    def inject_fault(self, raw_data):
        """
        Normal sensor data-kulla oru 'Error'-a insert pannum.
        """
        fault = random.choice(self.fault_types)
        modified_data = raw_data.copy()

        if fault == "VOLTAGE_SAG":
            modified_data['voltage'] *= 0.8 # 20% drop
        elif fault == "SENSOR_BIAS":
            modified_data['current'] += 50.0 # Fake high current
            
        return modified_data, fault