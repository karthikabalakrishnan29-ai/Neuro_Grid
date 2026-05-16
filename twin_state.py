import datetime

class DigitalTwinState:
    def __init__(self):
        # Current status of all assets
        self.state = {
            "timestamp": None,
            "solar_output": 0.0,
            "wind_output": 0.0,
            "load_demand": 0.0,
            "battery_soc": 0.0,
            "net_balance": 0.0,
            "is_faulty": False
        }

    def update_state(self, telemetry_data):
        """IoT layer-la irunthu vara data-va state-ukku update pannum"""
        self.state["timestamp"] = datetime.datetime.now().isoformat()
        self.state["solar_output"] = telemetry_data.get("solar", 0.0)
        self.state["wind_output"] = telemetry_data.get("wind", 0.0)
        self.state["load_demand"] = telemetry_data.get("load", 0.0)
        self.state["battery_soc"] = telemetry_data.get("soc", 0.0)
        self.state["net_balance"] = (self.state["solar_output"] + self.state["wind_output"]) - self.state["load_demand"]
        
    def get_current_state(self):
        return self.state