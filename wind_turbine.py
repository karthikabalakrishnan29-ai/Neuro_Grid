import numpy as np
class WindTurbine:
    def __init__(self, rated_power=10.0, cut_in_speed=3.0, cut_out_speed=25.0):
        self.rated_power = rated_power
        self.cut_in_speed = cut_in_speed
        self.cut_out_speed = cut_out_speed

    def calculate_power(self, wind_speed):
        """
        Wind speed cut-in limit-ku mela iruntha thaan power generate aagum.
        """
        if wind_speed < self.cut_in_speed or wind_speed > self.cut_out_speed:
            return 0.0
        
        # Cubic relation simulation (Simplified)
        # P = 0.5 * rho * A * Cp * v^3
        normalized_speed = (wind_speed - self.cut_in_speed) / (12.0 - self.cut_in_speed)
        power = self.rated_power * (normalized_speed ** 3)
        
        return round(min(power, self.rated_power), 4) # Max rated power-a thaanda koodathu