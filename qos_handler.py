class QoSHandler:
    def __init__(self):
        # 0: At most once, 1: At least once, 2: Exactly once
        self.levels = {
            "telemetry": 1,
            "critical_alerts": 2,
            "logs": 0
        }
    
    def get_level(self, msg_type):
        return self.levels.get(msg_type, 1)