import random

class WindForecaster:
    def predict_wind_power(self, current_wind):
        """
        Wind stochastic-ah irukkum, so random variation 
        with trend use pannalam.
        """
        variation = random.uniform(-0.5, 0.5)
        predicted = current_wind + variation
        return round(max(0, predicted), 4)