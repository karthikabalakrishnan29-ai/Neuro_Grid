class LoadModel:
    def __init__(self, scaling_factor=1.0):
        self.scaling_factor = scaling_factor

    def get_active_load(self, raw_power_value):
        # Dataset-la irukka values-a simulation scale-ku matha
        return round(raw_power_value * self.scaling_factor, 4)