from utils.logger import logger

class ShadowDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.desired_state = {}
        self.reported_state = {}

    def report(self, status):
        """Actual hardware report panra data"""
        self.reported_state = status
        logger.info(f"Shadow [{self.device_id}] updated via telemetry.")

    def set_desired(self, commands):
        """EMS (Intelligence Layer) anupra command-a store panna"""
        self.desired_state = commands
        logger.info(f"New desired state set for {self.device_id}: {commands}")