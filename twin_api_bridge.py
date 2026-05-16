class TwinAPIBridge:
    def __init__(self, twin_state):
        self.twin_state = twin_state

    def fetch_dashboard_data(self):
        """Dashboard-ku thevaiyana format-la data-va ready panna"""
        state = self.twin_state.get_current_state()
        return {
            "main_kpis": {
                "Generation": state["solar_output"] + state["wind_output"],
                "Demand": state["load_demand"],
                "Storage": state["battery_soc"]
            },
            "status": "Healthy" if not state["is_faulty"] else "Action Required"
        }