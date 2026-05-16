from core_layer.digital_twin.twin_state import DigitalTwinState

class TwinService:
    def __init__(self):
        self.twin = DigitalTwinState()

    def get_latest_metrics(self):
        # Digital Twin layer-la irunthu data-va fetch pannum
        state = self.twin.get_current_state()
        return state