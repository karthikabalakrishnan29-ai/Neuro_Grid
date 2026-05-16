from utils.logger import logger

class LoadSheddingManager:
    def __init__(self):
        # 1: High Priority (Hospital/Server), 3: Low Priority (AC/Decorative Lights)
        self.load_priorities = {
            "Critical_Zone": 1,
            "Residential_Zone": 2,
            "Commercial_Zone": 3
        }

    def execute_shedding(self, deficit_kw):
        """Power deficit-a poruthu loads-a cut pannum"""
        actions = []
        if deficit_kw > 10.0:
            actions.append({"device": "Commercial_Zone", "action": "OFF"})
            logger.warning("Stage 1 Load Shedding: Cutting Commercial Zone.")
        
        if deficit_kw > 25.0:
            actions.append({"device": "Residential_Zone", "action": "OFF"})
            logger.error("Stage 2 Load Shedding: Cutting Residential Zone.")
            
        return actions