from utils.logger import logger

class WhatIfAnalyzer:
    def __init__(self):
        self.scenarios = {
            "NO_SOLAR": {"solar_mult": 0.0, "desc": "Total Cloud Cover / Night"},
            "PEAK_LOAD": {"load_mult": 2.5, "desc": "Industrial Peak Demand"},
            "LOW_BATTERY": {"soc_limit": 10.0, "desc": "Battery Critical Level"}
        }

    def run_scenario(self, scenario_name, current_state):
        """
        Input state-a modify panni impact-a predict pannum.
        """
        if scenario_name in self.scenarios:
            config = self.scenarios[scenario_name]
            logger.info(f"Running What-If: {config['desc']}")
            
            # Logic to calculate impact
            impact = {
                "new_net_power": current_state['net_p'] * config.get('solar_mult', 1.0),
                "stability_score": "LOW" if scenario_name == "NO_SOLAR" else "STABLE"
            }
            return impact
        return None