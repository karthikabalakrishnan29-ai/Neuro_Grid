import numpy as np
from utils.logger import logger

class MILPOptimizer:
    def __init__(self):
        logger.info("MILP Optimizer Initialized.")

    def optimize_dispatch(self, forecast_data, current_soc):
        """
        Simple Optimization Logic:
        1. Renewable power priority.
        2. If excess, charge battery.
        3. If deficit, discharge battery.
        4. If still deficit, use Diesel Generator.
        """
        solar = forecast_data.get('solar', 0)
        wind = forecast_data.get('wind', 0)
        load = forecast_data.get('load', 0)
        
        total_gen = solar + wind
        net_balance = total_gen - load
        
        action = "BALANCED"
        if net_balance > 0:
            action = "CHARGE_BATTERY" if current_soc < 95 else "CURTAIL_RENEWABLE"
        else:
            action = "DISCHARGE_BATTERY" if current_soc > 20 else "START_GENERATOR"
            
        return {
            "optimal_action": action,
            "net_flow": round(net_balance, 4),
            "target_soc": 95 if action == "CHARGE" else 20
        }