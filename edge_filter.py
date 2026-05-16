class EdgeFilter:
    def __init__(self, threshold=0.01):
        self.last_values = {}
        self.threshold = threshold

    def should_filter(self, device_id, new_value):
        """Value change perusa illana filter pannidum (Data optimization)"""
        last_val = self.last_values.get(device_id)
        if last_val is not None and abs(new_value - last_val) < self.threshold:
            return True
        self.last_values[device_id] = new_value
        return False