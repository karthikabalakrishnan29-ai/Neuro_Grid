import numpy as np
import datetime
from utils.logger import logger

class PriceSimulator:
    def __init__(self):
        # Base price: ₹6.0 per kWh
        self.base_price = 6.0

    def get_dynamic_price(self, current_demand_kw, current_solar_kw):
        """
        Demand adhigama iruntha price yerum.
        Solar generation adhigama iruntha price korayum.
        """
        hour = datetime.datetime.now().hour
        
        # Peak hours (Evening 6-10 PM) price multiplier
        peak_multiplier = 1.5 if 18 <= hour <= 22 else 1.0
        
        # Supply-Demand Gap impact
        gap = current_demand_kw - current_solar_kw
        gap_impact = (gap / 100.0) * 0.5 # Every 100kW gap adds ₹0.5
        
        final_price = (self.base_price + gap_impact) * peak_multiplier
        return round(max(2.0, final_price), 2) # Minimum ₹2.0