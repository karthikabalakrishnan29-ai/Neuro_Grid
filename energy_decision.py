from utils.logger import logger

class EnergyDecisionMaker:
    def __init__(self, battery_threshold=20):
        self.battery_threshold = battery_threshold

    def decide_action(self, state, current_price):
        """
        State: {solar, wind, load, soc}
        Logic: 
        1. Solar/Wind iruntha athaiyae use pannu.
        2. Price adhigama iruntha (PEAK), battery-a discharge pannu.
        3. Price kuraiva iruntha (OFF-PEAK), battery-a grid-la irunthu charge pannu.
        """
        net_gen = state['solar'] + state['wind']
        demand = state['load']
        soc = state['soc']
        
        decision = "NEUTRAL"
        
        if net_gen > demand:
            decision = "STORE_EXCESS" if soc < 95 else "EXPORT_TO_GRID"
        else:
            # Deficit scenario
            if current_price > 8.0 and soc > self.battery_threshold:
                decision = "BATTERY_DISCHARGE" # Price high, use battery
            elif current_price < 5.0 and soc < 80:
                decision = "GRID_CHARGE_BATTERY" # Price low, charge battery
            else:
                decision = "IMPORT_FROM_GRID"
                
        logger.info(f"EMS Decision: {decision} at Price: ₹{current_price}")
        return decision