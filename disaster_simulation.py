class DisasterSimulator:
    def trigger_blackout(self):
        """
        Main utility grid cut aana enna aagum?
        """
        return {
            "grid_status": "OFFLINE",
            "mode": "ISLAND_MODE",
            "priority_loads": "ON",
            "non_essential_loads": "SHEDDED"
        }

    def simulate_cyber_attack(self):
        """
        IoT data-va manipulate panna logic.
        """
        return {"alert": "Unauthorized Control Signal Detected", "security_level": "HIGH"}