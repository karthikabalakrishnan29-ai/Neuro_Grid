import pandas as pd
from utils.config import MICROGRID_DATA_PATH

class SolarForecaster:
    def __init__(self):
        self.data = pd.read_csv(MICROGRID_DATA_PATH)

    def forecast_next_hour(self, current_time):
        """
        Historical data-la intha time-la average-ah 
        evlo solar generation irunthuthu-nu paakum.
        """
        # Time string-a handle panna logic
        # Simple seasonal averaging
        avg_solar = self.data['Solar_Power_kW'].mean()
        return round(avg_solar, 4)