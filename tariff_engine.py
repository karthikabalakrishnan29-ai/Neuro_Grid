import datetime
import pandas as pd

class TariffEngine:
    def __init__(self):
        # Peak hours-la rate adhigama irukkum
        self.rates = {
            "OFF_PEAK": 4.5,  # ₹/kWh (Night time)
            "NORMAL": 6.0,    # ₹/kWh (Day time)
            "PEAK": 9.5       # ₹/kWh (Evening 6 PM - 10 PM)
        }

    def get_current_price(self, timestamp=None):
        if timestamp is None:
            hour = datetime.datetime.now().hour
        else:
            hour = pd.to_datetime(timestamp).hour

        if 18 <= hour <= 22:
            return self.rates["PEAK"]
        elif 0 <= hour <= 6:
            return self.rates["OFF_PEAK"]
        else:
            return self.rates["NORMAL"]