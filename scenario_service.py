class ScenarioService:
    def trigger_what_if(self, scenario_type: str):
        """
        'GRID_FAILURE' or 'HIGH_RENEWABLE' scenarios-a simulate panna
        """
        if scenario_type == "GRID_FAILURE":
            return {"action": "ISLAND_MODE", "result": "Microgrid running on Battery"}
        return {"action": "NORMAL", "result": "Grid Synchronized"}