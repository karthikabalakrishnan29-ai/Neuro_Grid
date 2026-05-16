import numpy as np

class SolarPanel:
    def __init__(self, efficiency=0.18, area=20, temp_coeff=-0.004):
        self.efficiency = efficiency
        self.area = area
        self.temp_coeff = temp_coeff  # Temperature increase aana efficiency kuraiyum

    def calculate_power(self, irradiance, temperature):
        """
        P_pv = Area * Efficiency * Irradiance * [1 + Coeff * (T_cell - T_ref)]
        """
        if irradiance <= 0:
            return 0.0
            
        # Standard Reference Temperature = 25 C
        temp_correction = 1 + self.temp_coeff * (temperature - 25)
        power_output = self.area * self.efficiency * irradiance * temp_correction
        
        return round(max(0, power_output / 1000), 4) # kW-la return pannum