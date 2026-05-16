import numpy as np

class PowerFlowSimulator:
    def __init__(self, line_resistance=0.05):
        self.r = line_resistance # Ohms per km

    def calculate_losses(self, current_amps, distance_km=1.0):
        """P_loss = I^2 * R"""
        loss = (current_amps ** 2) * (self.r * distance_km)
        return round(loss / 1000, 4) # kW-la return pannum

    def estimate_voltage_drop(self, current_amps, base_voltage=230):
        """V_drop = I * R"""
        v_drop = current_amps * self.r
        return round(base_voltage - v_drop, 2)