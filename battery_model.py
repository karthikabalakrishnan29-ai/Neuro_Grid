import numpy as np
class BatteryModel:
    def __init__(self, capacity_kwh=50, initial_soc=70, efficiency=0.95):
        self.capacity = capacity_kwh
        self.soc = initial_soc
        self.efficiency = efficiency

    def update_soc(self, net_power, duration_hrs=0.25):
        """
        net_power > 0: Charging
        net_power < 0: Discharging
        """
        # Energy in kWh
        energy_change = net_power * duration_hrs
        
        if energy_change > 0:
            # Charging loss
            actual_change = energy_change * self.efficiency
        else:
            # Discharging loss
            actual_change = energy_change / self.efficiency
            
        soc_change_percent = (actual_change / self.capacity) * 100
        self.soc = np.clip(self.soc + soc_change_percent, 10, 95) # 10% to 95% safety range
        
        return round(self.soc, 2)