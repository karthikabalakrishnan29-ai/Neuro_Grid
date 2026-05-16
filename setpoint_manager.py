class SetpointManager:
    def __init__(self):
        # Default operational setpoints
        self.setpoints = {
            "inverter_v": 230.0,
            "grid_freq": 50.0,
            "max_battery_discharge": 0.8, # 80% discharge limit
            "solar_curtailment": 1.0      # 100% allowed
        }

    def update_setpoint(self, key, value):
        if key in self.setpoints:
            self.setpoints[key] = value
            return True
        return False

    def get_all_setpoints(self):
        return self.setpoints