import time
from .energy_balance import EnergyBalancer
from core_layer.assets.battery_model import BatteryModel
from utils.logger import logger

class MicrogridSim:
    def __init__(self):
        self.balancer = EnergyBalancer()
        self.battery = BatteryModel()
        self.results_log = []

    def run_step(self, timestamp, solar, wind, load):
        """Oru time-step (e.g., 15 mins) simulation-a run pannum"""
        # 1. Calculate Balance
        net_p = self.balancer.calculate_balance(solar, wind, load)
        
        # 2. Update Battery SOC
        new_soc = self.battery.update_soc(net_p, duration_hrs=0.25)
        
        # 3. Log data
        step_data = {
            "time": timestamp,
            "net_power": net_p,
            "soc": new_soc,
            "status": "Normal" if new_soc > 20 else "Low Battery"
        }
        self.results_log.append(step_data)
        return step_data

# Example initialization
# sim = MicrogridSim()