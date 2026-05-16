class EdgeAggregator:
    def __init__(self):
        self.buffer = []

    def aggregate_readings(self, readings):
        """Average calculate panni latency-a kuraikkum"""
        if not readings: return 0.0
        return sum([r['value'] for r in readings]) / len(readings)