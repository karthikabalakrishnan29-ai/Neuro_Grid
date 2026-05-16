import time
from utils.logger import logger

class SyncEngine:
    def __init__(self, twin_state, shadow_device):
        self.twin_state = twin_state
        self.shadow = shadow_device

    def synchronize(self):
        """Reported state-a virtual twin-oda sync pannuvom"""
        reported = self.shadow.reported_state
        if reported:
            self.twin_state.update_state(reported)
            return True
        return False